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
  actors.*
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
  count(*)
from
  actors
  join roles on actors.id = roles.actor_id
  join movies_genres on roles.movie_id = movies_genres.movie_id
where
  movies_genres.genre = 'War'


-- voglio sapere quali attori non hanno mai recitato in un film di guerra --
select
  actors.*
from
  actors,
  roles
where
  actors.id = roles.actor_id
  and roles.movie_id not in (
    select
      movie_id
    from
      movies_genres
    where
      movies_genres.genre = 'War'
  )