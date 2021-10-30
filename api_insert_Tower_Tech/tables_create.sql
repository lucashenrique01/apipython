CREATE TABLE tbCapturaDeDados (
	idCapturaDeDado 	INT,
    fkComputador 		INT,
    fkTorre 			INT,
	PRIMARY KEY (idCapturaDeDado, fkComputador, fkTorre),
    usuarioMaq 			VARCHAR(45),
    cpuPorcentual		DECIMAL(5,2),
    ramPorcentual		DECIMAL(5,2),
    discoPorcentual		DECIMAL(5,2),
    internet 			VARCHAR(13),
    dataHora 			DATETIME
);