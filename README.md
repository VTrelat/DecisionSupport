### Modèle

#### Actions

On représente les actions par une matrice $(A_{i,j})_{1\leq i\leq 14, 1 \leq j \leq 3}$ telle que :

$$\begin{cases*}
A_{i,j} = 1 \text{ si la variante $j$ de l'action $i$ est sélectionnée}\\
A_{i,j} = 0 \text{ sinon}
\end{cases*}$$

On a donc $A\in\mathcal{M}_{14,3}(\{0,1\})$ et

$$\forall 1 \leq i \leq 14 \quad A_{i, 1} + A_{i, 2} + A_{i, 3} \in \{0,1\}$$
i.e. on ne peut pas sélectionner plusieurs variantes d'une même action.

#### Données

On représente les données des critères et des aléas par un tenseur d'ordre 4 $(D_{i,j,k_\alpha})_{1 \leq i \leq 14, 1 \leq j \leq 3, 1 \leq k \leq 3, 1 \leq \alpha \leq 3}$ tel que :

$D_{i,j,k_\alpha} \in \mathbb{R}$ représente la valeur du critère $k$ au niveau d'aléa $\alpha$ pour la variante $j$ de l'action $i$

En l'occurrence ici, on a 3 critères et 4 niveau d'aléa :

-   $k = 1$ : attractivité
-   $k = 2$ : risque d'inondation
-   $k = 3$ : environnement

#### Coûts

On représente les coûts par une matrice $(C_{i, j})_{1 \leq i \leq 14, 1 \leq j \leq 3}$ telle que :

$C_{i,j} \in \mathbb{R}_+$ représente le coût de la variante $j$ de l'action $i$.

Si $A$ est une matrice d'actions, le coût $C_i$ de l'action $i$ est donné par

$$C_i = \sum_{j = 1}^{3} A_{i,j} C_{i,j}$$

Le coût total est donc donné par :

$$C_\text{total}(A) = \langle A, C \rangle$$

> Remarque: on utilise le produit scalaire matriciel canonique, i.e.
> $$\langle A, C \rangle = \text{tr}(A^T \cdot C) = \sum_{i = 1}^{14} \sum_{j = 1}^{3} A_{i,j} C_{i,j}$$

#### Contributions

Soit $A$ une matrice d'actions (i.e. $A$ a bien les propriétés définies ci-dessus). On définit la contribution de $A$ pour le critère $k$ au niveau d'aléa $\alpha$ par :

$$\text{Contrib}_ {k_\alpha}(A, D) = \sum_{i=1}^{14} \sum_{j=1}^3 A_{i,j} D_{i,j,k_\alpha}$$

#### Ordre lexicographique

L'ordre lexicographique $<_ {lex}$ est défini de manière générale par :
$$\forall \vec{x} \forall \vec{y} \quad \vec{x} <_{lex} \vec{y} \equiv \exists k \forall i < k \quad x_i = y_i \land x_k < y_k$$

### Formulation du problème

#### Formulation pour résolution avec le simplex

On souhaite déterminer une famille d'actions à choisir de façon à maximiser les critères, et ce pour un coût inférieur à un certain seuil.

> La façon dont on souhaite maximiser les critères est la suivante :
>
> -   On commence par maximiser le premier critère (l'attractivité) ;
> -   Si deux actions ont la même attractivité, on maximise le deuxième critère (le risque d'inondation) ;
> -   Si deux actions ont la même attractivité et le même risque d'inondation, on maximise le troisième critère (l'environnement).
>
> On utilisera donc l'ordre lexigraphique $<_ {lex}$ sur les critères 1, 2 et 3 (dans cet ordre) pour comparer les actions.

Soit $\alpha$ un niveau d'aléa. Le problème se formule donc de la manière suivante.
On cherche une matrice d'actions $A$ telle que :

$$\begin{cases*}
(\text{Contrib}_ {k_\alpha}(A, D))_ {k \in \{1,2,3\}} = \underset{A'}{\max_ {lex}} \ (\text{Contrib}_ {k_\alpha}(A', D))_ {k \in \{1,2,3\}} \\
C_ {\text{tot}}(A) \leq C_\text{max}
\end{cases*}$$

> $\max_ {lex}$ est l'opérateur de maximisation pour l'ordre lexicographique.

Le fait que $A$ soit une matrice d'action ajoute les contraintes suivantes, pour tout $i \in \{1, \dots, 14\}$ :

$$
\begin{align*}
&A_{i, 1} + A_{i, 2} + A_{i, 3} &\leq 1\\
&-A_{i, 1} &\leq 0\\
&-A_{i, 2} &\leq 0\\
&-A_{i, 3} &\leq 0\\
\end{align*}
$$

#### Formulation pour résolution avec une recherche exhaustive (récursive)

Flemme
