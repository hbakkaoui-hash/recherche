/* Configuration MathJax commune aux pages-articles.
   IMPORTANT : délimiteurs avec antislash (\( \) et \[ \]) — surtout PAS de
   crochets/parenthèses nus, sinon le texte entre [ ] ou ( ) serait pris pour
   des formules. */
window.MathJax = {
  tex: {
    inlineMath: [['$', '$'], ['\\(', '\\)']],
    displayMath: [['$$', '$$'], ['\\[', '\\]']],
    macros: {
      lcm: "\\operatorname{lcm}",
      fpole: "\\infty^{*}"
    }
  },
  options: { skipHtmlTags: ['script', 'noscript', 'style', 'textarea'] }
};
