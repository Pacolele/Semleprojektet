/**
 * This is a minimal config.
 *
 * If you need the full config, get it from here:
 * https://unpkg.com/browse/tailwindcss@latest/stubs/defaultConfig.stub.js
 */

module.exports = {
    content: [
        /**
         * HTML. Paths to Django template files that will contain Tailwind CSS classes.
         */

        /*  Templates within theme app (<tailwind_app_name>/templates), e.g. base.html. */
        '../templates/**/*.html',

        /*
         * Main templates directory of the project (BASE_DIR/templates).
         * Adjust the following line to match your project structure.
         */
        '../../templates/**/*.html',

        /*
         * Templates in other django apps (BASE_DIR/<any_app_name>/templates).
         * Adjust the following line to match your project structure.
         */
        '../../**/templates/**/*.html',

        /**
         * JS: If you use Tailwind CSS in JavaScript, uncomment the following lines and make sure
         * patterns match your project structure.
         */
        /* JS 1: Ignore any JavaScript in node_modules folder. */
        // '!../../**/node_modules',
        /* JS 2: Process all JavaScript files in the project. */
        // '../../**/*.js',

        /**
         * Python: If you use Tailwind CSS classes in Python, uncomment the following line
         * and make sure the pattern below matches your project structure.
         */
        // '../../**/*.py'
    ],
    theme: {
        extend: {},
    },
    plugins: [
        /**
         * '@tailwindcss/forms' is the forms plugin that provides a minimal styling
         * for forms. If you don't like it or have own styling for forms,
         * comment the line below to disable '@tailwindcss/forms'.
         */
        require('@tailwindcss/forms'),
        require('@tailwindcss/typography'),
        require('@tailwindcss/aspect-ratio'),
        require('daisyui'),
    ],
    daisyui: {
      themes: [
        "bumblebee", 
        {
          'bumblebee-dark': {
            'color-scheme': 'dark',
            'primary': 'oklch(85% 0.199 91.936)',
            'primary-content': 'oklch(42% 0.095 57.708)',
            'secondary': 'oklch(75% 0.183 55.934)',
            'secondary-content': 'oklch(40% 0.123 38.172)',
            'accent': 'oklch(0% 0 0)',
            'accent-content': 'oklch(100% 0 0)',
            'neutral': 'oklch(37% 0.034 259.733)',
            'neutral-content': 'oklch(92% 0.003 48.717)',
            'base-100': 'oklch(27% 0.041 260.031)',
            'base-200': 'oklch(27% 0.033 256.848)',
            'base-300': 'oklch(44% 0.043 257.281)',
            'base-content': 'oklch(98% 0.003 247.858)',
            'info': 'oklch(58% 0.158 241.966)',
            'info-content': 'oklch(90% 0.058 230.902)',
            'success': 'oklch(72% 0.219 149.579)',
            'success-content': 'oklch(37% 0.077 168.94)',
            'warning': 'oklch(82% 0.189 84.429)',
            'warning-content': 'oklch(41% 0.112 45.904)',
            'error': 'oklch(70% 0.191 22.216)',
            'error-content': 'oklch(39% 0.141 25.723)',
            '--rounded-box': '1rem',
            '--rounded-btn': '1rem',
            '--rounded-badge': '1rem',
            '--tab-border': '1px',
            '--btn-text-case': 'none',
          },
        },
      ],
      darkTheme: 'bumblebee-dark',
    },
}
