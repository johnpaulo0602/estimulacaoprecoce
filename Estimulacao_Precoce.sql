CREATE DATABASE Estimulacao_Precoce;
USE Estimulacao_Precoce;

-- Criando tabela Alunos com informações dos alunos

CREATE TABLE Alunos(
  IdAluno int primary key not null auto_increment,
  NomeCompleto varchar (50) not null,
  Telefone1 varchar(20) not null,
  Telefone2 varchar(20) not null,
  CPF varchar (20) not null unique,
  DataNascimento date not null,
  Sexo varchar (15) not null,
  Naturalidade varchar (20),
  UF varchar (5) not null,
  HipoteseDiagnostica varchar(800) not null
);

-- Criando tabela Turma com informações das turmas

CREATE TABLE Turma(
  IdTurma int primary key not null auto_increment,
  Identificacao varchar (30) not null,
  Turno varchar (20) not null,
  Professor varchar (50) not null
);

-- Criando tabela AlunoTurma com informações de alunos associados a turmas

CREATE TABLE AlunoTurma (
  IdAluno int not null,
  IdTurma int not null,
  primary key (IdAluno, IdTurma),
  foreign key (IdAluno) references Alunos(IdAluno) ON DELETE CASCADE,
  foreign key (IdTurma) references Turma(IdTurma) ON DELETE CASCADE
);

-- Criando tabela Professor com informações dos professores

CREATE TABLE Professor(
  IdProfessor int primary key not null auto_increment,
  NomeCompleto varchar(50) not null,
  IdTurma int not null,
  foreign key (IdTurma) references Turma(IdTurma)
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
