# Zveřejnění rodokmenu

Kořen Git repozitáře je složka `rodokmen`, tedy rodič složek `projekt` a `web_rodokmen`. Ve VS Code otevírej tuto složku. Historie původních commitů je zachovaná; po posunutí kořene se zdrojové soubory v příštím commitu objeví pod `projekt/`.

Do repozitáře patří zdrojové soubory projektu i hotový `web_rodokmen`. Závislosti, cache a pracovní zálohy dál vylučují soubory `.gitignore`.

## GitHub Pages

1. Commitni a pushni změny do větve `master` v `DominikKulich/rodokmen`.
2. Na GitHubu otevři **Settings → Pages → Build and deployment → Source: GitHub Actions**.
3. V **Custom domain** nastav `rodokmen.dominikkulich.cz`.
4. U správce DNS nastav CNAME `rodokmen` na `dominikkulich.github.io` (bez protokolu a cesty). Pokud používáš DNS WEDOS, změň jen záznamy pro subdoménu `rodokmen`; pro stejný název nesmí zůstat konfliktní A/AAAA. Změny aplikuj.
5. Po ověření domény a vystavení certifikátu zapni na GitHub Pages **Enforce HTTPS**.

Workflow `.github/workflows/pages.yml` publikuje výhradně obsah `web_rodokmen`, nikoli celý repozitář. Spouští se při pushi do `master` nebo `main`, který mění hotový web či workflow; lze ho spustit i ručně v **Actions → Rodokmen na GitHub Pages → Run workflow**.

Změny zdrojů je nejprve potřeba exportovat a sestavit. Nástroj `projekt/tools/export_local.py` potom aktualizuje `web_rodokmen`; tyto změny commitni a pushni. Samotné nasazení již nic nesestavuje.

GitHub Pages je veřejný web; CNAME ani `.nojekyll` nezajišťují přístupové heslo.

Oficiální postup: https://docs.github.com/en/pages/getting-started-with-github-pages/using-custom-workflows-with-github-pages
