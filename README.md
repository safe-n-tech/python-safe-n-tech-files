# python-safe-n-tech-files

Script qui a permit d'ajouter des ids aux ressources, n'est plus utilisé car les nouveaux articles sont créés avec un id.

## Contexte
Le site safe-n-tech est réalisé en Hugo, ce qui permet en autre de stocker le contenu dans des fichiers md tout en ayant des relations et des taxonomies.  
Cependant, l'identification d'un contenu se fait via son slug, et le slug est une propriété inconstante, modifiable.  
Pour permette une modification du titre et du slug d'un contenu sans casser les relations, il faut créer un champs identifiant constant.  
## Ajout des identifiants constant
Cet ensemble de scripts est là pour définir les identifiants (ici des uuid) sur les contenus et reporter les identifiants dans les contenus liés, ce qui permet de basculer les relations sur les id et non plus sur les slugs.
