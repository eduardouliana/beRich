create table sorteios_possiveis(
	id text,
	numeros text,
	id_sorteio numeric
);

create unique index sorteios_possiveis_unq on sorteios_possiveis(id);
