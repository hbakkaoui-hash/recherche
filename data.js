/* =====================================================================
   Données du site — modifie ce fichier pour ajouter du contenu.
   Pour chaque publication : remplis "zenodo" et "arxiv" quand tu as
   les liens (sinon laisse null, le bouton n'apparaît pas).
   ===================================================================== */

const PHYSIQUE = [
  {
    titre: "Unité 1 — Discontinuité d'existence des particules quantiques",
    tags: ["quant-ph", "HDEQ", "intermittent quantum existence", "existence qubit", "gating function"],
    resume: `Introduit l'<strong>Hypothèse de Discontinuité de l'Existence Quantique</strong>
      (HDEQ) : l'existence active d'un système quantique serait intermittente, alternant
      par cycles de durée caractéristique $\\tau_0$ entre une phase de dynamique
      hamiltonienne et une phase de suspension dynamique. L'évolution intermittente,
      implémentée par une dilatation contrôlée $\\hat{U}(\\tau_0)$ sur
      $\\mathcal{H}_{\\mathrm{sys}}\\otimes\\mathcal{H}_{\\mathrm{temp}}$, est globalement
      unitaire ; un critère de stabilité de phase sélectionne les états propres du
      hamiltonien effectif $H_{\\mathrm{eff}}$ comme base privilégiée.`,
    pdfFR: "papers/u1_FR.pdf",
    pdfEN: "papers/u1_EN.pdf",
    zenodo: "https://doi.org/10.5281/zenodo.20671269",
    arxiv: null,
    html: "articles/unite1.html"
  },
  {
    titre: "Unité 2 — Un champ de dualité d'échelle compactifié : régularisation et inflation",
    tags: ["gr-qc", "astro-ph.CO", "compactified scale duality", "dualité d'échelle compactifiée", "regular black hole", "de Sitter core", "natural inflation"],
    resume: `Étudie si un unique champ de dualité d'échelle $\\psi$ — issu de la
      compactification de l'axe d'échelle en un cercle, couplé non minimalement à la
      courbure via $f\\propto 1+\\beta\\cos\\psi$ et portant un potentiel borné
      $V=\\alpha(1-\\cos\\psi)$ — peut à la fois régulariser la singularité de
      Schwarzschild et engendrer l'inflation. Le pôle unifié engendre un cœur de Sitter
      exact ($w=-1$, $K=24H^4$ fini), de stabilité radiale gouvernée par un seuil exact
      $\\beta_c=-1/3$.`,
    pdfFR: "papers/u2_FR.pdf",
    pdfEN: "papers/u2_EN.pdf",
    zenodo: "https://doi.org/10.5281/zenodo.20671328",
    arxiv: null,
    html: "articles/unite2.html"
  },
  {
    titre: "Unité 3 — Dualité d'échelle compactifiée : synthèse",
    tags: ["gr-qc", "astro-ph.CO", "quant-ph", "compactified scale duality", "dualité d'échelle compactifiée", "scale compactification", "natural inflation", "regular black holes", "HDEQ"],
    resume: `Synthèse du programme. Mécanique quantique et relativité générale
      émergeraient d'une même structure : la compactification des axes d'échelle, spatial
      et temporel, en cercles — $\\mathcal{M}=M_{3+1}\\times S^1_\\psi\\times S^1_\\chi$
      sous $\\mathbb{Z}_2\\times\\mathbb{Z}_2$. Un seul champ d'échelle, couplé via
      $f=1+\\beta(\\cos\\psi+\\cos\\chi)$ et $V=\\alpha(2-\\cos\\psi-\\cos\\chi)$, gouverne
      les deux régimes : inflation naturelle prédictive $(n_s,r)$, clôture des trous noirs
      réguliers dans le secteur statique, et un pont reliant l'axe temporel à la HDEQ.`,
    pdfFR: "papers/u3_FR.pdf",
    pdfEN: "papers/u3_EN.pdf",
    zenodo: "https://doi.org/10.5281/zenodo.20671446",
    arxiv: null,
    html: "articles/unite3.html"
  },
  {
    titre: "Unité 4 — Effondrement gravitationnel, faux vide métastable, isocourbure et spectre Mukhanov–Sasaki exact",
    tags: ["gr-qc", "astro-ph.CO", "compactified scale duality", "dualité d'échelle compactifiée", "false vacuum decay", "Mukhanov–Sasaki spectrum", "GUT-scale inflation"],
    resume: `Un unique champ d'échelle sur
      $\\mathcal{M}=M_{3+1}\\times S^1_\\psi\\times S^1_\\chi$ gouverne gravité, cosmologie
      et secteur quantique. L'action de décroissance du faux vide de Sitter est obtenue
      exactement sous forme close $B_{\\mathrm{HM}}=24\\pi^2(3\\beta+\\tfrac12)^2/\\alpha$,
      s'annulant au seuil $\\beta_c=-1/6$ ; la trajectoire diagonale est démontrée
      géodésique ; le spectre scalaire est résolu mode par mode (Mukhanov–Sasaki), fixant
      une échelle d'inflation GUT $V^{1/4}\\approx 1{,}1\\text{–}1{,}5\\times10^{16}$ GeV.`,
    pdfFR: "papers/u4_FR.pdf",
    pdfEN: "papers/u4_EN.pdf",
    zenodo: "https://doi.org/10.5281/zenodo.20671560",
    arxiv: null,
    html: "articles/unite4.html"
  },
  {
    titre: "Unité 5 — Compactification sphérique de l'espace d'échelle",
    tags: ["hep-th", "gr-qc", "quant-ph", "compactified scale duality", "dualité d'échelle compactifiée", "spherical compactification", "scale arrow", "Planck pole"],
    resume: `Fait de l'échelle une dimension interne compacte et en déduit la seule action
      qu'elle autorise. Là où le programme antérieur enroulait l'échelle en un tore —
      collant le plus petit et le plus grand en un point unique — cette unité sépare ce
      point en <em>deux pôles distincts</em> (Planck d'un côté, l'infini de l'autre),
      portant l'objet compact à une <strong>sphère</strong>. Ce geste, à lui seul, libère
      une flèche d'échelle dirigée, au prix de l'enroulement et de la dualité d'inversion.`,
    pdfFR: "papers/u5_FR.pdf",
    pdfEN: "papers/u5_EN.pdf",
    zenodo: "https://doi.org/10.5281/zenodo.20671840",
    arxiv: null,
    html: "articles/unite5.html"
  },
  {
    titre: "Unité 6 — Une origine 5D de la dualité d'échelle : une cinquième dimension d'espace-temps compactifiée",
    tags: ["hep-th", "gr-qc"],
    resume: `Les Unités 1–3 traitaient les axes d'échelle comme cibles internes d'un
      modèle sigma — <em>pas</em> des dimensions d'espace-temps — pour éviter fantômes et
      courbes de genre temps fermées. Cette unité teste le choix opposé : promouvoir l'axe
      d'échelle logarithmique en une véritable <strong>cinquième dimension d'espace-temps
      compactifiée</strong>. Par réduction de Kaluza–Klein d'une métrique 5D déformée le
      long d'un cercle d'échelle compact (algèbre tensorielle vérifiée symboliquement, tour
      KK calculée), on demande si ce plongement régénère l'action du corpus et si le
      couplage non minimal $\\beta$ peut être <em>prédit</em> plutôt qu'ajusté.`,
    pdfFR: "papers/u6_FR.pdf",
    pdfEN: "papers/u6_EN.pdf",
    zenodo: "https://doi.org/10.5281/zenodo.21142465",
    arxiv: null,
    html: "articles/unite6.html"
  }
];

const MATHS = [
  {
    titre: "Une famille paramétrique de nombres premiers $p=k\\,m(m+1)+e+2kq$",
    tags: ["math.NT", "arXiv"],
    resume: `Étude de la famille paramétrique $p_{k,m,e,q}=k\\,m(m+1)+e+2kq$
      ($k,m\\in\\mathbb{N}^{*}$, $e\\in\\{+1,-1\\}$, $q\\in\\mathbb{Z}$), qui généralise le
      fait élémentaire que tout premier $p>3$ vérifie $p\\equiv\\pm 1 \\ (\\mathrm{mod}\\ 6)$.
      Le travail établit des propriétés modulaires, des certificats de primalité
      inconditionnels (Pocklington–Lehmer) pour une sous-famille, et montre que de prétendues
      corrélations spectrales avec les zéros de $\\zeta$ sont des artefacts statistiques. Des
      résultats conditionnels (GRH, Bateman–Horn, RH) bornent $|q_{\\min}|$ ; une constante
      géométrique $\\approx 1/(4\\sqrt{k})$ est validée numériquement jusqu'à $10^{8}$.`,
    pdfFR: null,
    pdfEN: null,
    zenodo: null,
    arxiv: "https://arxiv.org/abs/2606.16189",
    html: "articles/primes-parametriques.html"
  },
  {
    titre: "Certificats de primalité inconditionnels pour la famille hexagonale 3-lisse $p=3m(m+1)+1$",
    tags: ["math.GM", "arXiv"],
    resume: `Étude de la sous-famille $p=3m(m+1)+1$ avec $m=2^{a}3^{b}-1$ — une tranche
      3-lisse des nombres hexagonaux centrés $3m^2+3m+1=(m+1)^3-m^3$ — sous l'angle de la
      certification de primalité (Pocklington–Lehmer). La 3-lissité de $m+1=2^{a}3^{b}$ fournit
      un diviseur entièrement factorisé $F=2^{a}3^{b+1}$ de $p-1$ avec $F>\\sqrt{p}$, réduisant
      le certificat à deux témoins ($q=2,3$). Résultat principal : une caractérisation
      déterministe exacte des deux témoins canoniques — $w_2=5$ valide ssi
      $a-b\\equiv 1,2\\ (\\mathrm{mod}\\ 4)$ (réciprocité quadratique), $w_3=7$ valide ssi
      $m\\not\\equiv 2\\ (\\mathrm{mod}\\ 7)$ (réciprocité cubique dans $\\mathbb{Z}[\\omega]$).
      Démonstration : quatre certificats inconditionnels, le plus grand un premier de
      $29\\,998$ chiffres décimaux.`,
    pdfFR: null,
    pdfEN: null,
    zenodo: null,
    arxiv: "https://arxiv.org/abs/2606.18859",
    html: "articles/primes-hexagonaux.html"
  },
  {
    titre: "Suite $\\tau^{+}(n)$ — OEIS A397433 (fonction d'Erdős–Ford)",
    tags: ["math.NT", "OEIS"],
    resume: `Contribution <strong>publiée à l'OEIS</strong> : la suite <strong>A397433</strong>,
      qui recense la fonction $\\tau^{+}(n)$ — le nombre de blocs dyadiques $[2^k,2^{k+1})$
      contenant au moins un diviseur de $n$ (soit le nombre de valeurs distinctes de
      $\\lfloor\\log_2 d\\rfloor$ quand $d$ parcourt les diviseurs de $n$). Reliée au problème
      d'Erdős #448 (conjecture $\\tau^{+}(n)<\\varepsilon\\,\\tau(n)$ réfutée par Erdős–Tenenbaum,
      1981). Publiée après relecture éditoriale, avec b-file de 10 000 termes et programmes
      vérifiés (PARI, Python, Mathematica).`,
    pdfFR: null,
    pdfEN: null,
    zenodo: null,
    arxiv: null,
    lien: { url: "https://oeis.org/A397433", label: "OEIS A397433" }
  },
  {
    titre: "Spirales de premiers — visualisation interactive",
    tags: ["Visualisation", "Interactif"],
    resume: `Une visualisation interactive des <strong>familles paramétriques de nombres
      premiers</strong> $p=k\\,m(m+1)+e+2kq$ (dont la famille hexagonale $p=3m(m+1)+1$).
      Chaque terme est placé sur une spirale ; les premiers ressortent en points lumineux,
      révélant la structure et la densité de la famille (par défaut, près de 20 % de premiers
      sur 10 000 termes). Réglez les paramètres, la palette et la rotation, affichez ou non
      les non-premiers, et observez la répartition en spirale. Un outil pour <em>donner à
      voir</em> la géométrie qui sous-tend les papiers arXiv — avec export PNG.`,
    pdfFR: null,
    pdfEN: null,
    zenodo: null,
    arxiv: null,
    html: "spirale-premiers.html"
  },
  {
    titre: "Familles hexagonales de premiers — visualisation interactive",
    tags: ["Visualisation", "Interactif"],
    resume: `Une carte interactive des premiers sur le <strong>réseau hexagonal centré</strong>
      ($3n^2+3n+1=(n+1)^3-n^3$) : chaque premier $p$ est coloré selon sa décomposition
      canonique $p=3n(n+1)+\\varepsilon+6q$ (à $|q|$ minimal). Les premiers se répartissent le
      long des 6 diagonales et des couches concentriques ; isoler une famille
      $(\\varepsilon,q)$ met en évidence sa géométrie propre et la symétrie d'ordre 6 du réseau.
      Réglez le nombre d'étages, activez le réseau triangulé, les diagonales ou le remplissage
      — avec export PNG.`,
    pdfFR: null,
    pdfEN: null,
    zenodo: null,
    arxiv: null,
    html: "hexagones-premiers.html"
  },
  {
    titre: "Note — Problème d'Erdős #458 : réduction, classification et vérification jusqu'à $10^{12}$",
    tags: ["math.NT"],
    resume: `Erdős et Graham demandent si $[1,\\ldots,p_{k+1}-1] < p_k\\,[1,\\ldots,p_k]$
      pour tout $k\\ge 1$, où $[1,\\ldots,n]=\\lcm(1,\\ldots,n)$ et $p_k$ est le $k$-ième
      nombre premier. La note réduit la question à la cohabitation de puissances de
      premiers dans un même intervalle entre premiers consécutifs, classifie toutes les
      configurations pouvant produire un contre-exemple, et vérifie l'inégalité pour tout
      $k$ avec $p_{k+1}\\le 10^{12}$ : exactement cinq intervalles contiennent plus d'une
      puissance de premier, le plus grand rapport étant $6/7$ à l'intervalle $(7,11)$.`,
    pdfFR: null,
    pdfEN: "papers/erdos458_EN.pdf",
    zenodo: null,
    arxiv: null,
    html: "articles/erdos458.html"
  },
  {
    titre: "Contributions Lean — google-deepmind/formal-conjectures",
    tags: ["Lean 4", "Mathlib"],
    resume: `Formalisation de problèmes d'Erdős en <strong>Lean 4</strong> au sein du dépôt
      <em>formal-conjectures</em> de Google DeepMind. Ces formalisations traduisent l'énoncé
      d'un problème en un langage <strong>vérifié par ordinateur</strong> (Lean 4 / Mathlib),
      garantissant sa correction logique ligne à ligne — une étape vers des mathématiques dont
      chaque déduction est certifiée par la machine. Première contribution fusionnée (PR #4274,
      problème #448), sur un dépôt qui rassemble de nombreuses conjectures ainsi mises en forme.`,
    pdfFR: null,
    pdfEN: null,
    zenodo: null,
    arxiv: null,
    lien: { url: "https://github.com/google-deepmind/formal-conjectures", label: "Le dépôt" }
  }
];

const PROJETS = [
  {
    titre: "BakTaxi",
    tags: ["Application web", "PWA", "Supabase"],
    resume: `Plateforme web de mise en relation entre <strong>chauffeurs de taxi</strong>
      et clients (anciennement TAXI-LINK, puis TaxiLoc). Application installable (PWA),
      base de données Supabase, fonctionnement hors-ligne.`,
    pdfFR: null,
    pdfEN: null,
    zenodo: null,
    arxiv: null,
    lien: { url: "https://hbakkaoui-hash.github.io/baktaxi/", label: "Ouvrir l'application" }
  }
];
