import csv
from django.core.management.base import BaseCommand, CommandError
from semlerating.forms import SemlorForm
from semlerating.models import Semlor


class Command(BaseCommand):

    def add_arguments(self, parser):
        parser.add_argument("file_path", nargs=1, type=str)

    def handle(self, *args, **options):
        self.file_path = options["file_path"][0]
        self.prepare()
        self.main()
        self.finalize()

    def prepare(self):
        self.imported_counter = 0
        self.skipped_counter = 0

    def main(self):
        self.stdout.write("=== Importing semlor into DB ===")

        with open(self.file_path, mode="r", encoding='utf-8-sig') as f:
            reader = csv.DictReader(f, delimiter=";")
            for index, row in enumerate(reader):
                # Converts to True or False
                cleaned_row = {
                    'bakery': row['Bakery'].strip(),
                    'city': row['City'].strip(),
                    'picture_name': row['Picture'].strip(),
                    'vegan': row['Vegan'] == 'T',
                    'price': row['Price'].strip().replace(',', '.'),
                    'kind': row['Kind'].strip(),
                }
                print(cleaned_row)

                if not Semlor.objects.filter(
                    bakery=cleaned_row['bakery'],
                    city=cleaned_row['city'],
                    kind=cleaned_row['kind'],
                ).exists():
                    form = SemlorForm(data=cleaned_row)
                    if form.is_valid():
                        form.save()
                        self.imported_counter += 1
                    else:
                        self.stderr.write(f"Errors import semlor\n")
                        self.stderr.write(f"{form.errors.as_json()}\n")
                else:
                    self.skipped_counter += 1

    def finalize(self):
        print(f"------------------------- \n Imports: {
              self.imported_counter} \n Skipped: {self.skipped_counter}")
