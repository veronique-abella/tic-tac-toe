import pygame
import sys

pygame.init()

NOIR = (255, 255, 255)
BLANC = (0, 0, 0)
BLEU = (0, 0, 255)

LARGEUR_FENETRE = 300
HAUTEUR_FENETRE = 350
TAILLE_CASE = 100
TIC_TAC_TOE = [[None, None, None], [None, None, None], [None, None, None]]
joueur_actuel = 'X'
fenetre = pygame.display.set_mode((LARGEUR_FENETRE, HAUTEUR_FENETRE))
pygame.display.set_caption('Tic Tac Toe')

font = pygame.font.Font(None, 36)

def dessiner_grille():
    fenetre.fill(BLANC)
    for ligne in range(1, 3):
        pygame.draw.line(fenetre, NOIR, (0, ligne * TAILLE_CASE), (LARGEUR_FENETRE, ligne * TAILLE_CASE), 3)
        pygame.draw.line(fenetre, NOIR, (ligne * TAILLE_CASE, 0), (ligne * TAILLE_CASE, HAUTEUR_FENETRE - 50), 3)

def dessiner_symboles():
    for ligne in range(3):
        for colonne in range(3):
            if TIC_TAC_TOE[ligne][colonne] == 'X':
                pygame.draw.line(fenetre, NOIR, (colonne * TAILLE_CASE + 15, ligne * TAILLE_CASE + 15),
                                 (colonne * TAILLE_CASE + TAILLE_CASE - 15, ligne * TAILLE_CASE + TAILLE_CASE - 15), 3)
                pygame.draw.line(fenetre, NOIR, (colonne * TAILLE_CASE + 15, ligne * TAILLE_CASE + TAILLE_CASE - 15),
                                 (colonne * TAILLE_CASE + TAILLE_CASE - 15, ligne * TAILLE_CASE + 15), 3)
            elif TIC_TAC_TOE[ligne][colonne] == 'O':
                pygame.draw.circle(fenetre, NOIR, (int(colonne * TAILLE_CASE + TAILLE_CASE / 2),
                                                   int(ligne * TAILLE_CASE + TAILLE_CASE / 2)), 35, 3)

def verifier_victoire():
    for ligne in range(3):
        if TIC_TAC_TOE[ligne][0] == TIC_TAC_TOE[ligne][1] == TIC_TAC_TOE[ligne][2] and TIC_TAC_TOE[ligne][0] is not None:
            return TIC_TAC_TOE[ligne][0]
    for colonne in range(3):
        if TIC_TAC_TOE[0][colonne] == TIC_TAC_TOE[1][colonne] == TIC_TAC_TOE[2][colonne] and TIC_TAC_TOE[0][colonne] is not None:
            return TIC_TAC_TOE[0][colonne]
    if TIC_TAC_TOE[0][0] == TIC_TAC_TOE[1][1] == TIC_TAC_TOE[2][2] and TIC_TAC_TOE[0][0] is not None:
        return TIC_TAC_TOE[0][0]
    if TIC_TAC_TOE[0][2] == TIC_TAC_TOE[1][1] == TIC_TAC_TOE[2][0] and TIC_TAC_TOE[0][2] is not None:
        return TIC_TAC_TOE[0][2]
    for ligne in range(3):
        for colonne in range(3):
            if TIC_TAC_TOE[ligne][colonne] is None:
                return None
    return 'Match nul'

def afficher_bouton_nouvelle_partie():
    texte_bouton = font.render('Nouvelle partie', True, NOIR)
    texte_rect = texte_bouton.get_rect(center=(LARGEUR_FENETRE // 2, HAUTEUR_FENETRE - 25))
    fenetre.blit(texte_bouton, texte_rect)
    return texte_rect

while True:
    fenetre.fill(BLANC)  

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            x, y = pygame.mouse.get_pos()
            bouton_nouvelle_partie = afficher_bouton_nouvelle_partie()  
            if bouton_nouvelle_partie.collidepoint(x, y):
                TIC_TAC_TOE = [[None, None, None], [None, None, None], [None, None, None]]
                joueur_actuel = 'X'
            elif verifier_victoire() is None:
                ligne = y // TAILLE_CASE
                colonne = x // TAILLE_CASE
                if TIC_TAC_TOE[ligne][colonne] is None:
                    TIC_TAC_TOE[ligne][colonne] = joueur_actuel
                    if joueur_actuel == 'X':
                        joueur_actuel = 'O'
                    else:
                        joueur_actuel = 'X'

    dessiner_grille()
    dessiner_symboles()

    texte_bouton = font.render('Nouvelle partie', True, NOIR)
    texte_rect = texte_bouton.get_rect(center=(LARGEUR_FENETRE // 2, HAUTEUR_FENETRE - 25))
    fenetre.blit(texte_bouton, texte_rect)

    if verifier_victoire() is not None:
        victoire = verifier_victoire()
        texte = font.render(f'{victoire} a gagné!', True, BLEU)
        texte_rect = texte.get_rect(center=(LARGEUR_FENETRE // 2, HAUTEUR_FENETRE // 2))
        fenetre.blit(texte, texte_rect)

    pygame.display.flip()

