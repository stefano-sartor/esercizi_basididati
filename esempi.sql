-- voglio sapere quali attori hanno avuto un ruolo di dottore e in quale film --
select
  actors.*,
  movies.name,
  roles.role
from
  actors,
  movies,
  roles
where
  actors.id = roles.actor_id
  and roles.movie_id = movies.id
  and roles.role like '%Doctor%'

-- voglio sapere quali attori hanno recitato in un film di guerra --
select
  distinct actors.*
from
  actors,
  roles,
  movies_genres
where
  actors.id = roles.actor_id
  and roles.movie_id = movies_genres.movie_id
  and movies_genres.genre = 'War'

-- meglio, usando join --
select
  distinct actors.*
from
  actors
  join roles on actors.id = roles.actor_id
  join movies_genres on roles.movie_id = movies_genres.movie_id
where
  movies_genres.genre = 'War'
order by actors.id


-- voglio sapere quali attori non hanno mai recitato in un film di guerra

-- N.B. devo usare distinct perche' un attore deve può comparire più volte in un film
-- con diversi ruoli
select
  distinct actors.*
from
  actors
  join roles on actors.id = roles.actor_id
where
  roles.movie_id not in (
    select
      movie_id
    from
      movies_genres
    where
      movies_genres.genre = 'War'
  )
  



-- dato un attore, recuperare la lista dei film in cui ha un ruolo --


-- quali generi ha partecipato ogni attore -- 


-- quanti film hanno fatto ogni coppia rigista, attore --


-- classifica di genere per anno, oppure per intervallo di anni --


-- dato un anno, che generi escono --


-- percentuale uomini e donne per genere --





-- tutto --
select actors.first_name as 'actor_first_name',
actors.last_name         as 'actor_last_name',
actors.gender            as 'actor_gender',
roles.role               as 'actor_role',
movies.name              as 'movie_name',
movies.year              as 'movie_year',
movies_genres.genre      as 'movie_genre',
directors.first_name     as 'direcor_first_name',
directors.last_name      as 'director_last_name'

from actors
join roles on actor_id = actors.id
join movies on roles.movie_id = roles.movie_id
join movies_directors on movies.id = movies_directors.movie_id
join directors on directors.id = movies_directors.director_id
join movies_genres on movies_genres.movie_id = movies.id
order by movies.id