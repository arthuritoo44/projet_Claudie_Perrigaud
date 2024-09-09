USE projet_claudie_perrigaud;

SELECT * FROM analyse_donnees;

-- Comptage du nombre total de dates dans la table
SELECT COUNT(*) AS total_enregistrements
FROM analyse_donnees;

-- Moyenne pour chaque indicateurs
SELECT 
    AVG(sessions) AS moyenne_sessions,
    AVG(totalUsers) AS moyenne_utilisateurs_totaux,
    AVG(screenPageViews) AS moyenne_pages_vues,
    AVG(averageSessionDuration) AS moyenne_duree_session,
    AVG(bounceRate) AS moyenne_taux_rebond,
    AVG(engagedSessions) AS moyenne_sessions_engagees,
    AVG(eventCount) AS moyenne_evenements
FROM analyse_donnees;

/* On peut retenir qu'en moyenne le nombre d'utilisateurs par jour est
 assez faible (~5) mais l'interaction est plutôt bonne car lorsqe l'utilisateur
 est sur le site il reste plus de 3 minutes et explore environ 13 pages.
 Le taux de rebond étant inférieur à 40% nous inique également cette tendance.
 En effet cela signifie que l'utilisateur ne quitte pas le site après avoir vu
 une seule page
*/

-- Somme des interactions sur Facebook et Instagram
SELECT 
    SUM(interactions_facebook) AS total_interactions_facebook,
    SUM(interactions_instagram) AS total_interactions_instagram
FROM analyse_donnees;
-- Interactions plus importante sur la plateforme Instagram (64% des interactions)
SELECT 
    SUM(visites_facebook + visites_instagram) AS total_visites, 
    DATE 
FROM 
    analyse_donnees 
WHERE 
    DATE BETWEEN '2024-08-01' AND '2024-08-31' 
GROUP BY 
    DATE;
    
SELECT 
    DATE, 
    (interactions_facebook / couverture_facebook) AS taux_engagement_facebook, 
    (interactions_instagram / couverture_instagram) AS taux_engagement_instagram 
FROM 
    analyse_donnees;

-- couverture plus importante sur instagram avec un taux d'engagment général
-- plus élevé et des pics plus importants.

-- Répartition des sessions par durée moyenne
SELECT 
    CASE
        WHEN averageSessionDuration < 60 THEN 'Moins de 1 minute'
        WHEN averageSessionDuration BETWEEN 60 AND 300 THEN 'Entre 1 et 5 minutes'
        ELSE 'Plus de 5 minutes'
    END AS categorie_duree_session,
    COUNT(*) AS nombre_sessions
FROM analyse_donnees
GROUP BY categorie_duree_session;
-- Session répartie entre les catégories (1/3 des sessions moins de 1 minutes)
-- on cherchera plus tard à comprendre pourquoi.


    

SELECT 
    DATE, 
    SUM(totalUsers) AS total_utilisateurs, 
    SUM(visites_facebook) AS total_visites_facebook, 
    SUM(visites_instagram) AS total_visites_instagram 
FROM 
    analyse_donnees 
GROUP BY 
    DATE;
-- Nombre de visites globales entre 0 et 10 utilisateurs par jour, pas
-- de différence globale entre les plateformes
SELECT 
    DATE, 
    (newUsers / totalUsers) AS taux_nouveaux_utilisateurs 
FROM 
    analyse_donnees 
WHERE 
    totalUsers > 0;
-- En majorité ce sont de nouveaux utilisateurs, intéressant pour la popularité mais
-- nécésitté également de fidéliser l'audience. 

SELECT 
    DATE, 
    (visites_facebook + visites_instagram) AS total_visites_reseaux_sociaux, 
    sessions AS total_sessions_site 
FROM 
    analyse_donnees;
-- Afin de pouvoir visualiser les tendances et comparer les résultats entre
-- le site internet et les réseaux nous allons continuer l'analyse via PowerBi.


