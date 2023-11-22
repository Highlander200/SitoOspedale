Un ospedale della provincia di Brindisi intende informatizzare la prenotazione di visite specialistiche ambulatoriali e di esami clinici.

Il sistema, una volta funzionante, dovrà consentire ai pazienti di prenotare le proprie visite e/o i propri esami clinici a distanza e al personale sanitario la gestione degli appuntamenti così da consentire una corretta distribuzione del lavoro tra medici e infermieri.

Una volta prenotata la visita o l’esame, il paziente potrà recarsi all’ospedale direttamente al reparto di competenza e ricevere il proprio servizio facendo visualizzare all’operatore il codice QR ottenuto in fase di prenotazione.

Alla fine della prestazione, l’esito sarà memorizzato nel sistema informatico dall’operatore sanitario. I risultati della visita o degli esami rimarranno visibili, in modo permanente, sia al paziente che all’operatore medico che si è occupato del caso. 

Trattandosi di dati sensibili, però, il paziente, qualora lo richiedesse, potrà richiedere la cancellazione di tutti i suoi dati personali ivi comprese tutte le visite specialistiche e tutti gli esami clinici effettuati nella struttura. 
Tale procedura dovrà essere svolta esclusivamente da un amministratore di sistema che ha accesso a tutti i dati.

Sulla base delle esigenze della struttura ospedaliera su descritte, sarà necessario realizzare una applicazione web con tre differenti tipi di utenti: amministratore, paziente e medico.

Per i pazienti sono disponibili le seguenti funzionalità:
- registrazione al portale;
- prenotazione visite specialistiche con data e orario, è necessario specificare anche un medico;
- prenotazione esami clinici; è possibile specificare un esame clinico da una lista e successivamente data e orario;
- visualizzazione visite ed esami clinici prenotati;
- visualizzazione visite ed esami clinici effettuati con relativo esito.

Per gli amministratori sono disponibili le seguenti funzionalità:
- cancellazione permanente dei dati personali degli utenti, ivi comprese le visite e gli esami;
- cancellazione permanente degli account.

Per i medici sono disponibili le seguenti funzionalità:
- visualizzazione elenco pazienti nelle varie giornate;
- inserimento esito visita medica ed esami clinici.

## SPECIFICA 1 - Scadenza 7 novembre 2023
Realizzare utilizzando solo HTML e CSS le seguenti pagine:
- La pagina “home page” contenente una descrizione generale della struttura ospedaliera e una navbar da cui è possibile visitare le seguenti pagine:
	* “I nostri servizi"
	  + Visite specialistiche
	  + Analisi di laboratorio
	* “I nostri medici”
  * “Accesso al cittadino”
- La pagina “Accesso al cittadino” dovrà contenere un form per effettuare il login tramite username (codice fiscale) e password e un collegamento alla pagina “Registrati”
- La pagina “Registrati” dovrà contenere un form per la registrazione di un nuovo utente (Nome, Cognome, Sesso, Data di Nascita, Luogo di Nascita, CF)
- La pagina “Prenota visita specialistica” che conterrà una tabella contenente l’elenco di tutte le visite specialistiche erogate con i relativi medici, a fianco ad ogni riga della tabella dovrà essere presente un bottone con scritto “prenota ora”.
- La pagina “Prenota analisi di laboratorio” che conterrà una tabella contenente l’elenco di tutte le analisi di laboratorio erogate, a fianco ad ogni riga della tabella dovrà essere presente un bottone con scritto “prenota ora”.

## SPECIFICA 2 - Scadenza 26 novembre 2023
Migrare su Flask l'applicazione richiesta nella specifica 1.

Attenzione: tutti i collegamenti devono continuare a funzionare.