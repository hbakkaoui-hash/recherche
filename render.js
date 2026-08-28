/* Construction des cartes à partir des données de data.js */

function lien(href, label, cls) {
  return `<a class="card-link ${cls || ''}" href="${href}" target="_blank" rel="noopener">${label}</a>`;
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
    </article>`;
}

function remplir(id, items) {
  const el = document.getElementById(id);
  if (el) el.innerHTML = items.map(carte).join('');
  const c = document.getElementById(id + '-count');
  if (c) c.textContent = items.length;
}

if (typeof PHYSIQUE !== 'undefined') remplir('physique-grid', PHYSIQUE);
if (typeof MATHS   !== 'undefined') remplir('maths-grid',   MATHS);
if (typeof PROJETS !== 'undefined') remplir('projets-grid', PROJETS);

const _y = document.getElementById('year');
if (_y) _y.textContent = new Date().getFullYear();
