CREATE DATABASE Estimulacao_Precoce;
USE Estimulacao_Precoce;

-- Criando tabela Alunos com informações dos alunos

CREATE TABLE Alunos(
  IdAluno int primary key not null auto_increment,
  NomeCompleto varchar (50) not null,
  CPF varchar (20) not null unique,
  DataNascimento date not null,
  Sexo varchar (15) not null,
  Mae varchar (40) not null,
  Pai varchar (40) not null,
  Matricula varchar (30) not null,
  Telefone1 varchar(20) not null,
  Telefone2 varchar(20) not null,
  Naturalidade varchar (20),
  UF varchar (5) not null,
  HipoteseDiagnostica varchar(800) not null
);

-- Criando tabela Turma com informações das turmas

CREATE TABLE Turma(
  NomeTurma varchar (30) primary key not null,
  Turno varchar (20) not null,
  Professor varchar (50) not null
);

-- Criando tabela AlunoTurma com informações de alunos associados a turmas


CREATE TABLE AlunoTurma (
  IdAluno int not null,
  NomeTurma_al varchar(30) not null,
  primary key (IdAluno, NomeTurma_al),
  foreign key (IdAluno) references Alunos(IdAluno) ON DELETE CASCADE,
  foreign key (NomeTurma_al) references Turma(NomeTurma) ON DELETE CASCADE
);

-- Criando tabela Professor com informações dos professores

CREATE TABLE Professor(
  NomeCompleto varchar(50) primary key not null,
  NomeTurma_Pr varchar(30) not null,
  foreign key (NomeTurma_Pr) references Turma(NomeTurma)
);

-- Criando tabela Endereco com informações dos endereços

CREATE TABLE endereco (
  idEndereco int primary key not null auto_increment,
  Cidade varchar (30) not null,
  Numero varchar (10) not null,
  UF varchar (5) not null,
  Endereco varchar (130) not null,
  CEP varchar (20) not null unique
);

-- Criando tabela AlunoEndereco com informações de alunos associados a endereços

CREATE TABLE AlunoEndereco (
  Aluno_idAluno int not null,
  Endereco_idEndereco int not null,
  primary key (Aluno_idAluno, Endereco_idEndereco),
  foreign key (Endereco_idEndereco) references endereco(idEndereco),
  foreign key (Aluno_idAluno) references Alunos(IdAluno) ON DELETE CASCADE
);
