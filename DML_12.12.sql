use CONSCESSIONARIA_BD;

insert into Cliente(nome, idade, rg) values
('Bruna', 25, 20700),
('Anderson', 19, 130000),
('Caio', 32, 1200),
('Andre', 30, 1036000),
('Rafael', 50, 6000000),
('Lucas', 60, 90000),
('Mariana', 28, 502300),
('João', 45, 750000),
('Paula', 35, 890000),
('Carlos', 40, 300500);

insert into Automovel(placa, renavam, anofab, fabricante, modelo, codcliente) values
('aaa1111', 100000, 2016, 'Fiat', 'Palio', 1),
('aaa2222', 200000, 2019, 'Fiat', 'Bravo', 1),
('aaa3333', 300000, 2016, 'Ford', 'Focus', 2),
('aaa4444', 500000, 2012, 'Ford', 'Ka', 3),
('aaa5555', 300000, 2018, 'Fiat', 'Punto', 4),
('bbb1111', 150000, 2015, 'Chevrolet', 'Onix', 5),
('bbb2222', 250000, 2020, 'Hyundai', 'HB20', 6),
('bbb3333', 350000, 2018, 'Toyota', 'Corolla', 7),
('bbb4444', 450000, 2019, 'Volkswagen', 'Gol', 8);

insert into Ocorrencia(descricao, autoplaca) values
('Colisão lateral na 410 Norte', 'aaa3333'),
('Pneu furado', 'aaa4444'),
('Bateria arriada, 216 Norte', 'aaa2222'),
('Guincho para oficina, carro na liga', 'aaa3333'),
('Retrovisor quebrado', 'bbb1111'),
('Arranhão na lateral direita', 'bbb2222'),
('Pane elétrica', 'bbb3333'),
('Falha no sistema de freios', 'bbb4444');