create table tbPartidas(
    id int auto_increment primary key,
    nickname varchar(45),
    jogoEscolhido varchar(60),
    restatusPartida char(10),
    frag var(10),
    dataPartida datetime
);
