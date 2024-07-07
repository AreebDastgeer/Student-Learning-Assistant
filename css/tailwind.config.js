/** @type {import('tailwindcss').Config} */
module.exports = {
  purge: ['./profiles/templates/**/*.html'],
  darkMode: false, // or 'media' or 'class'
  theme: {
    colors: { 
      'taupe':'#928586',
      'rosy':'#d09d8f',
      'champagne':'#EDDACF',
      'cambridge':'#88C49C',  
      'china':'#9C5C7B',
      'light':'#dcd4ca'
    },
    extend: {},
  },
  variants: {
    extend: {},
  },
  plugins: [],
}


