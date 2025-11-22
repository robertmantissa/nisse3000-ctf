# 🎄 Nisse 2000: Naughty-to-Nice CTF

Ett webbaserat CTF-spel (Capture The Flag) med jultema där du hackar dig från "Olydig" till "Snäll"!

## 📖 Bakgrund

Du har blivit rapporterad till Tomtens Olydig-lista av din chef Ola för att du tidrapporterat för sent för många gånger. Ditt uppdrag är att hacka Tomtens system "Nisse 2000" och ändra din status till Snäll innan julafton!

## 🎯 Mål

Hacka dig igenom 4 nivåer och ändra din status från "OLYDIG" till "SNÄLL" i Tomtens databas.

## 🚀 Kom igång

### Kör lokalt

1. Öppna `index.html` i din webbläsare
2. Alternativt, starta en enkel HTTP-server:

```bash
# Python 3
python3 -m http.server 8000

# Python 2
python -m SimpleHTTPServer 8000

# Node.js (om du har npx)
npx http-server
```

3. Öppna `http://localhost:8000` i webbläsaren

## 🎮 Nivåer

### Nivå 1: Svagt lösenord
- **Utmaning:** Hitta rätt lösenord för att logga in
- **Hint:** Tomten älskar sina renar...
- **Lösning:** ||rudolf||

### Nivå 2: URL-manipulation
- **Utmaning:** Få tillgång till Snälla barn-listan och Systemloggar
- **Hint:** Titta på URL-parametern `role=nisse`
- **Lösning:** ||Ändra `role=nisse` till `role=tomte` för Snälla barn-listan, eller `role=admin` för Systemloggar||

### Nivå 3: Information från loggar
- **Utmaning:** Hitta lösenordet till databas-admin
- **Hint:** Leta i systemloggarna efter ett testlösenord
- **Lösning:** ||Leta efter testadmin-lösenordet i loggen: julafton2024||

### Nivå 4: Ändra databasen
- **Utmaning:** Navigera till databas-sidan och ändra din status
- **Hint:** Leta i loggarna efter URL:en till databasen
- **Lösning:** ||Gå till `/admin/database.html?role=admin` och ange lösenord, sedan klicka på knappen för att ändra status||

## 📁 Filstruktur

```
nisse2000-ctf/
├── index.html              # Startsida
├── login.html              # Inloggningssida (Nivå 1)
├── dashboard.html          # Dashboard med URL-manipulation (Nivå 2)
├── loggar.html            # Systemloggar (Nivå 3)
├── database.html          # Databas-admin (Nivå 4)
├── snalla-barn.html       # Snälla barn-listan
├── presentinventering.html # Presentlager
├── schema.html            # Nisse-schema
├── ren-status.html        # Status för renarna
├── onskelista.html        # Önskelistor
├── style.css              # Jultema styling
└── README.md              # Denna fil
```

## 🎨 Features

- ✨ Vackert jultema med röd, grön och guld färgpalett
- 🎯 4 progressiva nivåer för olika svårighetsgrader
- 💡 Inbyggda hints för nybörjare
- 🎉 Animerad framgångseffekt när du klarar CTF:en
- 📱 Responsiv design för mobil och desktop
- 🔒 Realistisk säkerhetssimulering

## 🎓 Lärdomar

Detta CTF lär ut grundläggande hackingkoncept:

1. **Svaga lösenord** - Varför starka lösenord är viktiga
2. **URL-manipulation** - Hur parametrar kan manipuleras
3. **Information leakage** - Vikten av att inte exponera känslig information i loggar
4. **Åtkomstkontroll** - Skillnaden mellan frontend- och backend-säkerhet

## ⚠️ Säkerhetsnoteringar

Detta är ett **utbildningsspel** som visar dåliga säkerhetsmetoder. I verkligheten:

- ❌ Lagra ALDRIG lösenord i klartext
- ❌ Lita ALDRIG på frontend-validering för säkerhet
- ❌ Exponera ALDRIG känslig information i loggar
- ❌ Använd ALDRIG svaga/förutsägbara lösenord
- ✅ Implementera ordentlig backend-autentisering och auktorisering
- ✅ Använd HTTPS för alla känsliga operationer
- ✅ Implementera rate limiting och andra säkerhetsåtgärder

## 🎅 Tips för spelledare

Om du kör detta som en workshop eller tävling:

- Ge deltagare 30-45 minuter för att klara alla nivåer
- Uppmuntra att dela hints med varandra
- Diskutera säkerhetsimplikationerna efteråt
- Anpassa svårighetsgraden genom att dölja/visa hints

## 🎄 Credits

Skapad som ett roligt julCTF för att lära ut grundläggande web security-koncept.

God Jul och lycka till med hackingen! 🎅🎁

---

**Säkerhetsnivå:** ⭐☆☆☆☆ (Avsiktligt osäkert för utbildningssyfte)
