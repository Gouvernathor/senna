## Types de motions

Les motions de censure et de nomination sont divisées entre:
- celles qui concernent le chancelier et l'ensemble du gouvernement, dites entières (E)
- celles qui concernent un seul membre du gouvernement hors chancelier, dites partielles (P)

(Ensuite le réglement de l'assemblée peut faire des arrangements comme soumettre plusieurs motions partielles à un vote unique groupé.
Et rien n'empêche à une motion entière de re-nommer un ministre à son poste actuel.
Ou même de renommer sans aucune modification l'ensemble d'un gouvernement qui était responsable devant l'autre assemblée.)

Les motions de censure et de nomination se divisent aussi entre:
- celles qui prévoient un remplacement, dites motions de nomination ou de censure constructive (N)
- celles qui n'en prévoient pas, appelées motions de censure sans remplacement (C)

CE?, CP, NE, NP.

## Vrac

Peut-être juste ne pas faire de pétitions avec signatures permanentes, et faire des motions recevablse ou pas recevables en fonction des circonstances ?

Lors du renouvellement partiel ou total de l'assemblée devant laquelle le gvt est responsable, le gvt devient immédiatement minoritaire.
(Sauf si il était majo à l'assemblée et que le sénat le reprend, mais c'est pas vraiment une exception à la règle.)

TODO
Traiter le cas du gouvernement démissionnaire (cas de la censure entière sans remplacement, CE, mais aussi de la démission du chancelier), puisque si on fonctionne par motions et pas par pétitions, on n'a pas de remplacement automatique.
-> interdire les censures entières ? vraie possibilité mais ne solutionne pas tout
Il ne reste que la censure partielle, remplacée par la motion elle-même (de nomination), par le chancelier, ou par une nomination partielle ultérieure ; et la nomination entière.
Même si le chancelier fait quelque chose que le parlement aime pas, le parlement peut toujours adopter une résolution qui limite ses pouvoirs.
-> ou alors la CE et la démission du chancelier (et sa mort) ouvrent juste de droit le même genre de période qu'après un renouvellement de l'assemblée, sur le régime des gouvernements minoritaires ?

TODO
Traiter aussi le cas de la continuité gouvernementale, dans le cas où :
- le chancelier (ou un ministre, mais surtout le chancelier) meurt
- le chancelier démissionne avec effet immédiat (exemple Charles Michel)
- si on ressuscite la censure entière sans remplacement
- si on autorise somehow la censure partielle du chancelier, pour trahison ou sur déblocage CJR

Une motion de censure sans remplacement, sauf mention contraire, est déposée par le chancelier, ou par un membre de la chambre dans laquelle elle est recevable.
(Le dépot par le chancelier autorise généralement les motions parallèles, et elles se maintiennent malgré le retrait éventuel de la motion du gouvernement.)
TODO
Les motions de nomination partielles sont-elles déposables par le chancelier ? Si oui, et les totales ? Si oui, même quand il est minoritaire ?

Une motion de nomination entière (NE) est recevable :
- dans l'assemblée devant laquelle le gouvernement est responsable,
- OU devant une assemblée de plus grande priorité (quand le gvt est minoritaire : le sénat ; quand le gvt est responsable devant le sénat : l'assemblée),
- OU si les conditions sur le chancelier ont été levées par la CJR.

TODO peut-être supprimé
Une motion de censure entière sans remplacement (CE) est recevable :
- dans une assemblée où une motion de nomination entière (NE) est recevable
- mais uniquement:
  - si le gouvernement est majoritaire,
  - OU si elle est déposée par le chancelier.

Une motion de nomination partielle (NP) est recevable :
- à l'assemblée devant laquelle le gvt est responsable.

Si elle est déposée par le chancelier et si le réglement de l'assemblée le permet, elle (NP) peut être adoptée par une commission de l'assemblée.

Une motion de censure partielle sans remplacement (CP) est recevable :
- dans les mêmes conditions qu'une nomination partielle (NP),
- OU si les conditions ont été levées par la CJR.

Lorsque la CJR lève les conditions et que la censure est adoptée (quelle que soit la chambre), le visé ne peut plus être nommé au gouvernement pendant une certaine durée (1 an).

Lorsque le poste de chancelier est vacant, le président de l'assemblée nationale ou, à défaut, le président du sénat, assure l'intérim.


## Vote des motions

### première option/version

Les motions de censure et de nomination sont mises au vote successivement, dans l'ordre :
- toutes les partielles avant toutes les entières, [peut-être obsolète avec la prop Beta]
- celles de nomination sont votées par approbation, avant celles de censure sans remplacement (qui sont votées séparément a priori, mais les déposants peuvent s'arranger),
- sous réserve du point précédent, les partielles sont ordonnées par ordre de dépôt et les entières par nombre décroissant de signataires.

Une motion de censure sans remplacement n'est caduque que si aucun des membres du gvt qu'elle vise n'est encore au gouvernement,
et les nominations (qui sont votées par approbation mais au cas où), seulement si tous les postes qu'elle nomme ont été pourvus depuis le dépôt de la motion.
Les motions partielles ne font donc pas forcément tomber les motions entières, mais les nominations font tomber les censures sans remplacement.

### deuxième version/option, baptisée Beta

*Voir fichier annexe*

problème : comment constater qu'un gouvernement initialement majoritaire, ne l'est plus ?
-> réponse pour l'assemblée : l'opposition dépose une pétition de gouvernement, et même si la pétition du gouvenement sortant reste en tête, si elle n'obtient pas la majorité absolue, le gouvernement devient minoritaire.
-> réponse pour le sénat ?
(marquer dans les cas de figure)

## Types de gouvernements

Les situations de majorité sont, par priorité croissante :

m) gouvernement minoritaire dans les deux chambres, responsable devant l'assemblée
s) gouvernement majoritaire au sénat, minoritaire à l'assemblée, responsable devant le sénat
a) gouvernement majoritaire à l'assemblée, responsable devant l'assemblée

Les gouvernements m et a sont responsables devant l'assemblée nationale et nommée par elle. L'approbation du sénat, pour un gouvernement m, est facultative et ne sert que de filet de sécurité si il perd sa majorité absolue à l'assemblée.

## Toutes les situations possibles

Pour chaque cas de figure, à numéroter sur Sphinx, présenter comment Senna y répond, avec des renvois internes. Les situations sont :

- il existe une pétition de plus grande priorité que le gouvernement en place
  - gouvernement m, pétition s
  - gouvernement s, pétition a
- le gouvernement perd sa majorité
  - gouvernement a
  - gouvernement s
- l'assemblée est renouvelée
  - en partant d'un gouvernement a
  - d'un gouvernement s
  - d'un gouvernement m
- la majorité relative à l'assemblée change (création ou rupture d'une alliance minoritaire)
  - avec un gouvernement m
- la majorité absolue change au sein de la chambre dans laquelle le gouvernement est majoritaire
  - avec un gouvernement a
  - avec un gouvernement s
- sans changement de majorité, un changement de composition du gouvernement à l'initiative de la chambre devant laquelle il est majoritaire
  - parmi les ministres
    - avec l'accord du concerné
      - avec l'accord du chancelier
      - sans l'accord du chancelier
    - sans l'accord du concerné
      - avec l'accord du chancelier
      - sans l'accord du chancelier
  - du chancelier
    - avec son accord
    - sans son accord
- idem pour un gouvernement minoritaire
- le chancelier veut remplacer un de ses ministres au sein d'un gouvernement majoritaire
  - avec l'accord du concerné
    - avec l'accord de la chambre
    - sans l'accord de la chambre
  - sans l'accord du concerné
    - avec l'accord de la chambre
    - sans l'accord de la chambre
- idem pour un gouvernement minoritaire
- une démission
  - d'un ministre
    - avec l'accord du chancelier
    - sans l'accord du chancelier
  - du chancelier, individuellement
  - du chancelier, avec son gouvernement
- une affaire judiciaire devant la CJR
  - sur le chancelier
    - gouvernement m
    - gouvernement majoritaire
  - sur un ministre
    - gouvernement m
    - gouvernement majoritaire
- un scandale sans implication de la CJR
  - sur le chancelier
    - gouvernement m
    - gouvernement majoritaire
  - sur un ministre
    - gouvernement m
    - gouvernement majoritaire
