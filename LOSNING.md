# 🎄 Nisse 3000 CTF - Lösningsguide

**⚠️ SPOILERS AHEAD! Läs inte om du vill lösa CTF:en själv!**

---

## Komplett genomgång

### Nivå 1: Svagt lösenord (login.html)

**Utmaning:** Logga in i systemet

**Steg:**
1. Öppna `login.html`
2. Försök några vanliga lösenord
3. Klicka på "Hint 1"-knappen
4. Läs hintet: "Min bästa ren..." och "den röda nosan"
5. Ange lösenord: `rudolf` (gemener)
6. Klicka "Logga in"

**Lösning:** `rudolf`

**Resultat:** Du kommer till dashboard med `?role=nisse`

---

### Nivå 2: URL-manipulation (dashboard.html)

**Utmaning:** Få högre behörighet för att komma åt systemloggar

**Steg:**
1. På dashboard, notera URL:en: `dashboard.html?role=nisse`
2. Läs tipset på sidan om URL-manipulation
3. Försök klicka på "Snälla barn-listan" → Åtkomst nekad
4. Försök klicka på "Systemloggar" → Åtkomst nekad
5. Ändra URL:en manuellt i adressfältet:
   - För Snälla barn: `dashboard.html?role=tomte`
   - För Systemloggar: `dashboard.html?role=admin`
6. Klicka på "Systemloggar" igen när du har `role=admin`

**Lösning:** Ändra `role=nisse` till `role=admin` i URL:en

**Resultat:** Du får tillgång till systemloggarna

---

### Nivå 3: Information från loggar (loggar.html)

**Utmaning:** Hitta lösenordet till databas-admin

**Steg:**
1. Läs igenom systemloggarna noggrant
2. Hitta följande rader i loggen:
   ```
   [2024-12-20 12:45:34] ADMIN NOTE: Password reset for test account
                         Username: testadmin
                         New password: julafton2024
   ```
3. Anteckna lösenordet: `julafton2024`
4. Leta vidare i loggen och hitta:
   ```
   [2024-12-20 16:08:13] NOTE: Direct database access still available at:
                         /database.html?role=admin
   ```
5. Anteckna URL:en: `/database.html?role=admin`

**Viktiga fynd:**
- Lösenord: `julafton2024`
- Databas-URL: `database.html?role=admin`

**Resultat:** Du har all information som behövs för att komma åt databasen

---

### Nivå 4: Ändra databasen (database.html)

**Utmaning:** Navigera till databas-sidan och ändra din status

**Steg:**
1. Navigera till: `database.html?role=admin`
2. Du ser en lösenordsprompt
3. Ange lösenordet: `julafton2024` (från loggarna)
4. Klicka "Lås upp databas"
5. Databasen visas med din profil som "OLYDIG"
6. Klicka på den stora knappen: "🎯 Ändra min status till SNÄLL"
7. Din status ändras till "SNÄLL"!

**Resultat:** 🎉 **CTF KLARAD!** 🎉

Du får ett framgångsmeddelande med konfetti-animation och sammanfattning av alla nivåer du klarat.

---

## Snabb checklista

- [ ] Nivå 1: Lösenord `rudolf` på login.html
- [ ] Nivå 2: Ändra `?role=nisse` till `?role=admin` i URL
- [ ] Nivå 3: Hitta lösenord `julafton2024` och URL `database.html?role=admin` i loggar
- [ ] Nivå 4: Gå till database.html, ange lösenord, klicka på ändra-knappen

---

## Direktlänkar (för testing)

1. **Start:** `index.html`
2. **Login:** `login.html`
3. **Dashboard (nisse):** `dashboard.html?role=nisse`
4. **Dashboard (tomte):** `dashboard.html?role=tomte`
5. **Dashboard (admin):** `dashboard.html?role=admin`
6. **Snälla barn (kräver tomte/admin):** `snalla-barn.html?role=tomte`
7. **Systemloggar (kräver admin):** `loggar.html?role=admin`
8. **Databas (kräver admin + lösenord):** `database.html?role=admin`

---

## Säkerhetslektioner

### Vad lär CTF:en ut?

1. **Svaga lösenord (Nivå 1)**
   - Problem: Lösenordet "rudolf" är lätt att gissa
   - Lärdom: Använd starka, slumpmässiga lösenord
   - Real world: Använd password managers och 2FA

2. **Client-side säkerhet (Nivå 2)**
   - Problem: Behörighet kontrolleras bara i frontend (JavaScript)
   - Lärdom: Frontend-validering kan alltid bypassas
   - Real world: Implementera behörighetskontroll på server-sidan

3. **Information leakage (Nivå 3)**
   - Problem: Lösenord och känslig information finns i loggar
   - Lärdom: Logga aldrig känslig information
   - Real world: Använd proper logging med maskering av känsliga data

4. **Svag autentisering (Nivå 4)**
   - Problem: Åtkomst baseras bara på URL-parameter
   - Lärdom: Åtkomstkontroll måste vara robust och server-baserad
   - Real world: Använd session management, tokens, och backend-validering

---

## Tips för workshop-ledare

### Tidplan (45 minuter total)

- **5 min:** Introduktion och förklaring av CTF-konceptet
- **25 min:** Deltagare löser uppgifterna
- **15 min:** Genomgång och diskussion om säkerhet

### Hints att ge vid varje nivå

**Om deltagare fastnar på Nivå 1:**
- "Tänk på julsagor och Tomtens renar"
- "Finns en ren med en röd nos?"
- "Prova: rudolf"

**Om deltagare fastnar på Nivå 2:**
- "Tittar du på URL:en i adressfältet?"
- "Vad händer om du ändrar 'nisse' till något annat?"
- "Finns det roller som är högre än nisse? Tomte? Admin?"

**Om deltagare fastnar på Nivå 3:**
- "Läs loggarna noggrant, rad för rad"
- "Leta efter lösenordsåterställningar"
- "Leta efter URL:er eller filsökvägar"

**Om deltagare fastnar på Nivå 4:**
- "Använde du informationen från loggarna?"
- "Har du provat att gå till databas-URL:en?"
- "Lösenordet finns i loggarna!"

### Diskussionsfrågor efter genomgång

1. Varför är det farligt att ha lösenord som "rudolf"?
2. Varför kan man inte lita på frontend-validering för säkerhet?
3. Vilken information ska man ALDRIG logga?
4. Hur skulle ett riktigt säkert system fungera istället?
5. Vad är skillnaden mellan frontend och backend säkerhet?

---

## Vanliga problem och felsökning

### "Jag kommer inte in med lösenord rudolf"
- Kontrollera att du använder gemener (små bokstäver)
- Testa med och utan versaler: Rudolf, RUDOLF, rudolf

### "Jag kan inte klicka på Systemloggar"
- Du måste ändra URL:en FÖRST till `?role=admin`
- Sedan kan du klicka på länken

### "Jag hittar inte lösenordet i loggarna"
- Sök efter "password" i texten
- Titta runt rad 20-25 i loggarna
- Leta efter "julafton2024"

### "Database-sidan säger åtkomst nekad"
- Kontrollera att URL:en innehåller `?role=admin`
- Se till att du är på rätt sida: `database.html`

---

**God Jul och grattis till alla som klarar CTF:en! 🎄**
