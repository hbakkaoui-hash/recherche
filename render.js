/* Construction des cartes à partir des données de data.js */

function lien(href, label, cls) {
  return `<a class="card-link ${cls || ''}" href="${href}" target="_blank" rel="noopener">${label}</a>`;
}

/* Échappement HTML — indispensable pour les blocs BibTeX, qui contiennent
   des accolades, des esperluettes et des chevrons. */
function echapper(s) {
  return String(s)
    .replace(/&/g, '&amp;')
    .replace(/</g, '&lt;')
    .replace(/>/g, '&gt;');
}

/* Bloc BibTeX repliable + bouton « copier ». */
function bibtexHTML(item) {
  if (!item.bibtex) return '';
  return `
      <details class="bibtex">
        <summary>BibTeX</summary>
        <div class="bibtex-body">
          <button type="button" class="bibtex-copy">Copier</button>
          <pre class="bibtex-code">${echapper(item.bibtex)}</pre>
        </div>
      </details>`;
}

function carte(item) {
  const tags = (item.tags || [])
    .map(t => `<span class="tag">${t}</span>`).join('');

  const liens = [];
  if (item.arxiv)  liens.push(lien(item.arxiv,  'arXiv',         'link-arxiv'));
  if (item.zenodo) liens.push(lien(item.zenodo, 'Zenodo',        'link-zenodo'));
  if (item.pdfFR)  liens.push(lien(item.pdfFR,  'PDF (FR)',      'link-pdf'));
  if (item.pdfEN)  liens.push(lien(item.pdfEN,  'PDF (EN)',      'link-pdf'));
  if (item.lien)   liens.push(lien(item.lien.url, item.lien.label + ' →', 'link-ext'));
  if (Array.isArray(item.liens))
    item.liens.forEach(l => liens.push(lien(l.url, l.label + ' →', 'link-ext')));

  const liensHTML = liens.length
    ? `<div class="card-links">${liens.join('')}</div>`
    : '';

  const titre = item.html
    ? `<a class="card-title-link" href="${item.html}">${item.titre}<span class="arrow"> →</span></a>`
    : item.titre;

  return `
    <article class="card">
      <div class="card-tags">${tags}</div>
      <h3>${titre}</h3>
      <p class="card-resume">${item.resume}</p>
      ${liensHTML}
      ${bibtexHTML(item)}
    </article>`;
}

function remplir(id, items) {
  const el = document.getElementById(id);
  if (el) el.innerHTML = items.map(carte).join('');
  const c = document.getElementById(id + '-count');
  if (c) c.textContent = items.length;
}

/* Styles du bloc BibTeX injectés ici (styles.css n'est pas modifié). */
(function styleBibtex() {
  const css = `
  .bibtex { margin-top: .9rem; }
  .bibtex > summary { cursor: pointer; font-size: .85rem; letter-spacing: .04em;
    text-transform: uppercase; opacity: .75; user-select: none; }
  .bibtex > summary:hover { opacity: 1; }
  .bibtex-body { margin-top: .6rem; }
  .bibtex-code { margin: 0; padding: .85rem 1rem; overflow-x: auto;
    font-family: ui-monospace, SFMono-Regular, Menlo, Consolas, monospace;
    font-size: .78rem; line-height: 1.5; white-space: pre;
    background: rgba(0,0,0,.28); border: 1px solid rgba(255,255,255,.12);
    border-radius: 8px; }
  .bibtex-copy { display: block; margin: 0 0 .45rem auto;
    font: inherit; font-size: .72rem; padding: .2rem .6rem; cursor: pointer;
    color: inherit; background: rgba(255,255,255,.10);
    border: 1px solid rgba(255,255,255,.22); border-radius: 6px; }
  .bibtex-copy:hover { background: rgba(255,255,255,.20); }`;
  const el = document.createElement('style');
  el.textContent = css;
  document.head.appendChild(el);
})();

/* Bouton « copier » — un seul écouteur délégué pour toute la page. */
document.addEventListener('click', function (ev) {
  const btn = ev.target.closest && ev.target.closest('.bibtex-copy');
  if (!btn) return;
  const pre = btn.parentElement.querySelector('.bibtex-code');
  if (!pre) return;
  const texte = pre.textContent;
  const fini = () => {
    const avant = btn.textContent;
    btn.textContent = 'Copié';
    setTimeout(() => { btn.textContent = avant; }, 1600);
  };
  if (navigator.clipboard && navigator.clipboard.writeText) {
    navigator.clipboard.writeText(texte).then(fini, () => secours(texte, fini));
  } else {
    secours(texte, fini);
  }
});

/* Repli si l'API presse-papiers n'est pas disponible (http, vieux navigateurs). */
function secours(texte, fini) {
  const ta = document.createElement('textarea');
  ta.value = texte;
  ta.setAttribute('readonly', '');
  ta.style.position = 'fixed';
  ta.style.opacity = '0';
  document.body.appendChild(ta);
  ta.select();
  try { document.execCommand('copy'); fini(); } catch (e) { /* silencieux */ }
  document.body.removeChild(ta);
}

if (typeof PHYSIQUE !== 'undefined') remplir('physique-grid', PHYSIQUE);
if (typeof MATHS   !== 'undefined') remplir('maths-grid',   MATHS);
if (typeof PROJETS !== 'undefined') remplir('projets-grid', PROJETS);

const _y = document.getElementById('year');
if (_y) _y.textContent = new Date().getFullYear();
