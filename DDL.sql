CREATE TABLE likes (
  usersid            int(10) NOT NULL, 
  title_basicstconst int(10) NOT NULL, 
  PRIMARY KEY (usersid, 
  title_basicstconst));
CREATE TABLE title_principals (
  tconst            int(10) NOT NULL, 
  ordering          int(2) NOT NULL, 
  name_basicsnconst int(10) NOT NULL, 
  category          varchar(100) NOT NULL, 
  job               varchar(100), 
  characters        varchar(100), 
  img_url_asset     varchar(500), 
  PRIMARY KEY (tconst, 
  ordering));
CREATE TABLE users (
  id       int(10) NOT NULL AUTO_INCREMENT, 
  Username varchar(100) NOT NULL UNIQUE, 
  password varchar(20) NOT NULL, 
  is_admin int(1) NOT NULL, 
  PRIMARY KEY (id));
CREATE TABLE director (
  name_basicsnconst  int(10) NOT NULL, 
  title_basicstconst int(10) NOT NULL, 
  PRIMARY KEY (name_basicsnconst, 
  title_basicstconst));
CREATE TABLE title_akas (
  titleId         int(10) NOT NULL, 
  ordering        int(2) NOT NULL, 
  title           varchar(100) NOT NULL, 
  region          varchar(5), 
  language        varchar(10), 
  types           varchar(50), 
  attributes      varchar(100), 
  isOriginalTitle int(1) NOT NULL, 
  PRIMARY KEY (titleId, 
  ordering));
CREATE TABLE title_basics (
  tconst         int(10) NOT NULL AUTO_INCREMENT, 
  titleType      varchar(20) NOT NULL, 
  primaryTitle   varchar(200) NOT NULL, 
  originalTitle  varchar(200) NOT NULL, 
  isAdult        int(1) NOT NULL, 
  startYear      int(4) NOT NULL, 
  endYear        int(4), 
  runtimeMinutes int(4), 
  genres         varchar(100), 
  `Column`       int(10), 
  PRIMARY KEY (tconst));
CREATE TABLE title_ratings (
  tconst        int(10) NOT NULL, 
  averageRating double NOT NULL, 
  numVotes      int(7) NOT NULL, 
  PRIMARY KEY (tconst));
CREATE TABLE ListForWtachingLater (
  usersid            int(10) NOT NULL, 
  title_basicstconst int(10) NOT NULL, 
  PRIMARY KEY (usersid, 
  title_basicstconst));
CREATE TABLE title_episode (
  tconst        int(10) NOT NULL AUTO_INCREMENT, 
  parentTconst  int(10) NOT NULL, 
  seasonNumber  int(3), 
  episodeNumber int(3), 
  PRIMARY KEY (tconst));
CREATE TABLE name_basics (
  nconst            int(10) NOT NULL AUTO_INCREMENT, 
  PrimaryName       varchar(100) NOT NULL, 
  birthYear         int(4) NOT NULL, 
  deathYear         int(4), 
  primaryProfession varchar(200) NOT NULL, 
  img_url_asset     varchar(500), 
  PRIMARY KEY (nconst));
CREATE TABLE writer (
  name_basicsnconst  int(10) NOT NULL, 
  title_basicstconst int(10) NOT NULL, 
  PRIMARY KEY (name_basicsnconst, 
  title_basicstconst));
CREATE TABLE knownForTitles (
  name_basicsnconst  int(10) NOT NULL, 
  title_basicstconst int(10) NOT NULL, 
  PRIMARY KEY (name_basicsnconst, 
  title_basicstconst));
ALTER TABLE title_principals ADD CONSTRAINT FKtitle_prin203074 FOREIGN KEY (name_basicsnconst) REFERENCES name_basics (nconst);
ALTER TABLE title_ratings ADD CONSTRAINT FKtitle_rati976740 FOREIGN KEY (tconst) REFERENCES title_basics (tconst);
ALTER TABLE title_episode ADD CONSTRAINT FKtitle_epis595858 FOREIGN KEY (parentTconst) REFERENCES title_basics (tconst);
ALTER TABLE title_akas ADD CONSTRAINT FKtitle_akas925023 FOREIGN KEY (titleId, ordering) REFERENCES title_principals (tconst, ordering);
ALTER TABLE likes ADD CONSTRAINT FKlikes442757 FOREIGN KEY (usersid) REFERENCES users (id);
ALTER TABLE likes ADD CONSTRAINT FKlikes85493 FOREIGN KEY (title_basicstconst) REFERENCES title_basics (tconst);
ALTER TABLE ListForWtachingLater ADD CONSTRAINT FKListForWta155105 FOREIGN KEY (usersid) REFERENCES users (id);
ALTER TABLE ListForWtachingLater ADD CONSTRAINT FKListForWta487630 FOREIGN KEY (title_basicstconst) REFERENCES title_basics (tconst);
ALTER TABLE director ADD CONSTRAINT FKdirector47392 FOREIGN KEY (name_basicsnconst) REFERENCES name_basics (nconst);
ALTER TABLE director ADD CONSTRAINT FKdirector154772 FOREIGN KEY (title_basicstconst) REFERENCES title_basics (tconst);
ALTER TABLE writer ADD CONSTRAINT FKwriter428677 FOREIGN KEY (name_basicsnconst) REFERENCES name_basics (nconst);
ALTER TABLE writer ADD CONSTRAINT FKwriter536057 FOREIGN KEY (title_basicstconst) REFERENCES title_basics (tconst);
