// 既にあるカラーをインポート(https://tailwindcss.com/docs/customizing-colors)
const colors = require('tailwindcss/colors')

module.exports = {
  purge: [],
  darkMode: false, // or 'media' or 'class'
  theme: {
    extend: {
    },
    colors: {
      transparent: 'transparent',
      current: 'current',
      white: colors.white,
      red: colors.red,
      green: colors.green,
      blue: colors.blue,
      black: colors.black,
    },
    // backgroundImage: theme=>({
    //   'main-image': "url('../../media/main.jpg')",
    // }),

  },
  variants: {
    extend: {
    },
  },
  plugins: [
  ],
}
