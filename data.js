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
    bibtex: `@misc{bakkaoui2026unite1,
  author       = {Bakkaoui, Hassane},
  title        = {{Quantum Existence Discontinuity (HDEQ): A Framework for Intrinsic Decoherence and Preferred-Basis Selection}},
  year         = {2026},
  month        = jun,
  publisher    = {Zenodo},
  doi          = {10.5281/zenodo.20671269},
  url          = {https://doi.org/10.5281/zenodo.20671269}
}`,
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
    bibtex: `@misc{bakkaoui2026unite2,
  author       = {Bakkaoui, Hassane},
  title        = {{Compactified Scale Duality in Gravity: from the Singular Black Hole to Falsifiable Inflation}},
  year         = {2026},
  month        = jun,
  publisher    = {Zenodo},
  doi          = {10.5281/zenodo.20671328},
  url          = {https://doi.org/10.5281/zenodo.20671328}
}`,
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
    bibtex: `@misc{bakkaoui2026unite3,
  author       = {Bakkaoui, Hassane},
  title        = {{Compactified Scale Duality: a Geometric Route toward the Unification of the Quantum and Gravitation}},
  year         = {2026},
  month        = jun,
  publisher    = {Zenodo},
  doi          = {10.5281/zenodo.20671446},
  url          = {https://doi.org/10.5281/zenodo.20671446}
}`,
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
    bibtex: `@misc{bakkaoui2026unite4,
  author       = {Bakkaoui, Hassane},
  title        = {{Gravitational collapse, metastable false vacuum, isocurvature, and exact Mukhanov--Sasaki spectrum. A compactified scale-duality field: pole metastability and inflationary prediction}},
  year         = {2026},
  month        = jun,
  publisher    = {Zenodo},
  doi          = {10.5281/zenodo.20671560},
  url          = {https://doi.org/10.5281/zenodo.20671560}
}`,
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
    bibtex: `@misc{bakkaoui2026unite5,
  author       = {Bakkaoui, Hassane},
  title        = {{Unit 5 --- Spherical compactification of scale space: latitude as a directed renormalization coordinate, the $\\infty^{*}$ lock lifted at the cost of winding and duality}},
  year         = {2026},
  month        = jun,
  publisher    = {Zenodo},
  doi          = {10.5281/zenodo.20671840},
  url          = {https://doi.org/10.5281/zenodo.20671840}
}`,
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
    // <!-- DOI EN ATTENTE DU CONTRÔLE R4 -->
    // Aucun champ `bibtex` pour l'Unité 6 : deux DOI concurrents circulent
    // (10.5281/zenodo.21142465 dans le JSON-LD du site, 10.5281/zenodo.21142466
    // dans l'enregistrement Zenodo). Le bloc BibTeX ne sera écrit qu'après le
    // contrôle DOI de R4 — un BibTeX est fait pour être copié par des tiers.
    html: "articles/unite6.html"
  }
];

const MATHS = [
  {
    titre: "Une famille paramétrique de nombres premiers $p=k\\,m(m+1)+e+2kq$",
    tags: ["math.GM", "arXiv"],
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
    bibtex: `@misc{bakkaoui2026parametricprimes,
  author        = {Bakkaoui, Hassane},
  title         = {{A parametric family of primes $p=km(m+1)+\\varepsilon +2kq$: heuristic laws, conditional theorems, and unconditional primality certificates}},
  year          = {2026},
  eprint        = {2606.16189},
  archivePrefix = {arXiv},
  primaryClass  = {math.GM},
  doi           = {10.48550/arXiv.2606.16189},
  url           = {https://doi.org/10.48550/arXiv.2606.16189}
}`,
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
    bibtex: `@misc{bakkaoui2026hexagonalcertificates,
  author        = {Bakkaoui, Hassane},
  title         = {{Unconditional Primality Certificates for the Hexagonal 3-smooth Family p = 3m(m+1) + 1: Deterministic Pocklington Witnesses and Arithmetic Filters}},
  year          = {2026},
  eprint        = {2606.18859},
  archivePrefix = {arXiv},
  primaryClass  = {math.GM},
  doi           = {10.48550/arXiv.2606.18859},
  url           = {https://doi.org/10.48550/arXiv.2606.18859}
}`,
    html: "articles/primes-hexagonaux.html"
  },
  {
    titre: "Six suites OEIS — la répartition des diviseurs (Erdős #446, #448, #449)",
    tags: ["math.NT", "OEIS"],
    resume: `<strong>Six suites publiées à l'OEIS</strong> (juin–septembre 2026), toutes sur une
      même question : les diviseurs d'un entier sont-ils étalés ou groupés&nbsp;?
      <strong>#448</strong> — $\\tau^{+}(n)$, nombre d'octaves $[2^k,2^{k+1})$ contenant un diviseur
      de $n$ (A397433). <strong>#449</strong> — $r(n)$, paires de diviseurs $d \lt e \lt 2d$ (A399440,
      qui diffère de A174903 dès $n=60$). <strong>#446</strong> — les valeurs <em>rationnelles
      exactes</em> de $\\delta(n)$ et $\\delta_1(n)$ (A399690/691, A399697/698), rendues calculables
      par la périodicité de période $\\operatorname{ppcm}(n+1,\\dots,2n-1)$. Valeurs en arithmétique
      exacte, recoupées par deux algorithmes et une source indépendante (S.&nbsp;Cambie, #692).`,
    pdfFR: null,
    pdfEN: null,
    zenodo: null,
    arxiv: null,
    html: "articles/suites-oeis-erdos.html",
    bibtex: `@misc{oeisBakkaouiDivisors,
  author       = {Bakkaoui, Hassane},
  title        = {{Six sequences on the distribution of divisors (OEIS A397433, A399440, A399690, A399691, A399697, A399698)}},
  year         = {2026},
  howpublished = {The On-Line Encyclopedia of Integer Sequences (OEIS Foundation Inc.)},
  url          = {https://oeis.org/search?q=author:\\%22Hassane+Bakkaoui\\%22}
}`,
    liens: [
      { url: "https://oeis.org/search?q=author%3A%22Hassane+Bakkaoui%22", label: "Toutes les suites (OEIS)" },
      { url: "https://www.erdosproblems.com/446", label: "Problème #446" },
      { url: "https://www.erdosproblems.com/448", label: "Problème #448" },
      { url: "https://www.erdosproblems.com/449", label: "Problème #449" }
    ]
  },
  {
    titre: "Familles polygonales de premiers — explorateur interactif",
    tags: ["Visualisation", "Interactif"],
    resume: `Explorateur qui <strong>généralise à tout paramètre $k$</strong> : les entiers se
      rangent en <strong>polygones centrés à $2k$ côtés</strong> (le cas $k=3$ redonne le
      réseau hexagonal), et les premiers $p=k\\,n(n+1)+\\varepsilon+2kq$ sont coloriés selon
      leur décomposition canonique $(m,\\varepsilon,q)$ à $|q|$ minimal — généralisation de
      $p\\equiv\\pm1\\pmod{2k}$. Choisissez $k$, le nombre d'étages, isolez chaque famille
      $(\\varepsilon,q)$ ; sous 6 étages chaque point affiche son numéro — avec export PNG.`,
    pdfFR: null,
    pdfEN: null,
    zenodo: null,
    arxiv: null,
    html: "polygones-premiers.html"
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
    html: "articles/erdos458.html",
    bibtex: `@misc{bakkaoui2026erdos458,
  author       = {Bakkaoui, Hassane},
  title        = {{A reduction, a classification, and a verification up to $10^{12}$ for Erd\\H{o}s problem \\#458}},
  year         = {2026},
  month        = jun,
  publisher    = {Zenodo},
  doi          = {10.5281/zenodo.20671980},
  url          = {https://doi.org/10.5281/zenodo.20671980},
  note         = {Concept DOI (toutes versions)}
}`,
    liens: [
      { url: "https://doi.org/10.5281/zenodo.20671980", label: "DOI Zenodo" },
      { url: "https://www.erdosproblems.com/458", label: "Problème #458" }
    ]
  },
  {
    titre: "Contributions Lean — google-deepmind/formal-conjectures",
    tags: ["Lean 4", "Mathlib"],
    resume: `Formalisation d'énoncés de problèmes d'Erdős en <strong>Lean 4 / Mathlib</strong> au
      sein du dépôt <em>formal-conjectures</em> de Google DeepMind — des traductions vérifiées
      <strong>typographiquement</strong> par la machine, reliées à la base
      <em>teorth/erdosproblems</em> (site erdosproblems.com). <strong>Quatre problèmes.</strong>
      <strong>#448</strong> : cycle complet (formalisation fusionnée, référence OEIS, « Yes » sur la
      page du problème). <strong>#446</strong> : ordre de Ford et densité définie <em>par
      période</em> (PR #6429, en revue). <strong>#449</strong> : onze théorèmes dont neuf prouvés,
      deux <code>sorry</code> restants (PR #5210, en revue). <strong>#667</strong> : énoncé
      (PR #4370, en revue).`,
    pdfFR: null,
    pdfEN: null,
    zenodo: null,
    arxiv: null,
    html: "articles/formalisation-lean-erdos.html",
    bibtex: `@misc{formalconjectures2026erdos448,
  author       = {{The Formal Conjectures Authors}},
  title        = {{FormalConjectures/ErdosProblems/448.lean}},
  year         = {2026},
  howpublished = {D\\'ep\\^ot google-deepmind/formal-conjectures},
  url          = {https://github.com/google-deepmind/formal-conjectures/blob/main/FormalConjectures/ErdosProblems/448.lean},
  note         = {Contribution de Hassane Bakkaoui ; pull request \\#4274, fusionn\\'ee le 23 juin 2026}
}`,
    liens: [
      { url: "https://github.com/google-deepmind/formal-conjectures", label: "Le dépôt" },
      { url: "https://github.com/google-deepmind/formal-conjectures/pull/4274", label: "PR #4274 (#448)" },
      { url: "https://github.com/google-deepmind/formal-conjectures/pull/6429", label: "PR #6429 (#446)" },
      { url: "https://github.com/google-deepmind/formal-conjectures/pull/5210", label: "PR #5210 (#449)" },
      { url: "https://github.com/google-deepmind/formal-conjectures/pull/4370", label: "PR #4370 (#667)" }
    ]
  }
];

const PROJETS = [
  {
    titre: "Brickbak — bac à briques 3D",
    tags: ["Jeu éducatif", "3D", "Construction"],
    resume: `Un <strong>bac à briques 3D</strong> où l'on bâtit maisons, véhicules et animaux
      brique par brique. Catalogue riche (briques, pentes, portes, bonhomme, animaux),
      <strong>six décors</strong> — prairie, ville, plage, neige, désert, espace —, annulation,
      sauvegarde, partage et modèles d'exemple. Pensé pour la créativité et la motricité fine
      des enfants.`,
    pdfFR: null,
    pdfEN: null,
    zenodo: null,
    arxiv: null,
    lien: { url: "https://brickbak.vercel.app/", label: "Ouvrir l'application" }
  },
  {
    titre: "Kumibak — casse-tête 3D à pièces emboîtables",
    tags: ["Jeu éducatif", "3D", "Casse-tête"],
    resume: `Un casse-tête 3D inspiré des <strong>kumiki japonais</strong> : replacer dans le
      bon ordre des pièces de bois qui s'emboîtent en volume. Moteur d'emboîtement réel,
      profondeur d'imbrication réglable, trois niveaux — Découverte, Moyen, Hardcore. Un jeu
      de logique et de patience qui muscle la vision dans l'espace, pour petits et grands.`,
    pdfFR: null,
    pdfEN: null,
    zenodo: null,
    arxiv: null,
    lien: { url: "https://kumiki-tawny.vercel.app/", label: "Ouvrir l'application" }
  },
  {
    titre: "bakOccas' — véhicules d'occasion",
    tags: ["Application web", "Next.js", "Supabase"],
    resume: `Une place d'annonces automobile <strong>inversée</strong> : l'acheteur décrit ce
      qu'il cherche et reçoit ses correspondances, le vendeur voit qui cherche déjà son
      véhicule. Au cœur de l'app, un <strong>moteur de correspondance</strong> acheteur ↔
      vendeur : on vend à une demande réelle, pas dans le vide.`,
    pdfFR: null,
    pdfEN: null,
    zenodo: null,
    arxiv: null,
    lien: { url: "https://bakoccas.vercel.app/", label: "Ouvrir l'application" }
  },
  {
    titre: "BakTaxi — annonces entre professionnels du taxi",
    tags: ["Application web", "PWA", "Temps réel"],
    resume: `La place d'annonces des <strong>professionnels du taxi</strong> (Île-de-France) :
      location véhicule + licence, location-gérance, <strong>licence ADS</strong> seule,
      remplacement, vente de matériel. Annonces partagées en temps réel, filtres par zone et
      budget, et un score de compatibilité selon le profil. (Anciennement TAXI-LINK / TaxiLoc.)`,
    pdfFR: null,
    pdfEN: null,
    zenodo: null,
    arxiv: null,
    lien: { url: "https://hbakkaoui-hash.github.io/baktaxi/", label: "Ouvrir l'application" }
  },
  {
    titre: "Farāʾiḍ — calculateur successoral islamique",
    tags: ["Utilité publique", "Trilingue", "Gratuit"],
    resume: `Un calculateur qui répartit un héritage selon le <strong>droit successoral
      islamique</strong> (avis majoritaire) : tous les héritiers, actif net et déductions,
      exclusion (ḥajb), ʿawl et radd, options d'école, résultats détaillés et export PDF.
      Fiches pédagogiques (versets, sources). Trilingue AR · FR · EN,
      <strong>gratuit et sans publicité</strong>.`,
    pdfFR: null,
    pdfEN: null,
    zenodo: null,
    arxiv: null,
    lien: { url: "https://hbakkaoui-hash.github.io/faraid/", label: "Ouvrir l'application" }
  }
];
