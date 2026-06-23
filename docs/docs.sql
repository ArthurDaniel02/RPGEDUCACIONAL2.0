
CREATE VIEW UsuarioA AS
SELECT P.id, A.pessoa_ptr_id, P.nome, P.classe, P.nivel, A.moedas FROM personagem P INNER JOIN aluno A
ON P.id = A.pessoa_ptr_id;
SELECT * FROM UsuarioA;


CREATE VIEW PessoaA AS
SELECT P.id, A.pessoa_ptr_id, P.nome, P.cpf, A.moedas FROM pessoa P INNER JOIN aluno A
ON P.id = A.pessoa_ptr_id;
SELECT * FROM PessoaA;

CREATE VIEW Turma AS
SELECT D.id, P.pessoa_ptr_id, D.nome AS "Disciplina", P.nome, P.moedas FROM disciplina D INNER JOIN disciplina_alunos Par
ON D.id = Par.disciplina_id INNER JOIN PessoaA P
ON Par.aluno_id = P.pessoa_ptr_id;
SELECT * FROM Turma;

DELIMITER :3
CREATE PROCEDURE setar_dinheiro (IN id INT)
BEGIN
UPDATE aluno SET moedas = 300 WHERE pessoa_ptr_id = id;
END :3
DELIMITER ;
CALL setar_dinheiro(4);
SELECT * FROM PessoaA WHERE pessoa_ptr_id = 4;
drop procedure setar_dinheiro;

DELIMITER :3
CREATE TRIGGER tgr_dinheiro_default BEFORE INSERT
ON aluno FOR EACH ROW
BEGIN
    SET NEW.moedas = 50;
END :3
DELIMITER ;

set @@autocommit = 0;
DELIMITER :3
CREATE PROCEDURE compra_item (IN p_aluno_id INT, IN p_item_id INT)
BEGIN
    DECLARE v_dinheiro INT DEFAULT NULL;
    DECLARE v_custo INT DEFAULT NULL;
    SELECT moedas INTO v_dinheiro FROM aluno WHERE pessoa_ptr_id = p_aluno_id;
    SELECT preco INTO v_custo FROM item WHERE id = p_item_id;
    START TRANSACTION;
    IF v_dinheiro IS NULL OR v_custo IS NULL THEN
        ROLLBACK;
        SELECT 'Erro: Aluno ou Item não encontrado no banco de dados!' AS Status_Compra;
    ELSEIF v_custo > v_dinheiro THEN
        ROLLBACK;
        SELECT 'Erro: Saldo insuficiente!' AS Status_Compra;
    ELSE
        UPDATE aluno SET moedas = v_dinheiro - v_custo WHERE pessoa_ptr_id = p_aluno_id;
        INSERT INTO aluno_itens (aluno_id, item_id) VALUES (p_aluno_id, p_item_id); 
        COMMIT;
        SELECT 'Compra realizada com sucesso!' AS Status_Compra;
    END IF;
END :3
DELIMITER ;

drop procedure compra_item;

call compra_item(4,3);

select * from Turma;


DELIMITER :3
CREATE FUNCTION media_moeda (discid INT)
RETURNS DECIMAL(10, 2) DETERMINISTIC
BEGIN
DECLARE media DECIMAL(10, 2);
    SELECT AVG(moedas) INTO media FROM Turma WHERE id = discid;
    RETURN media;
END :3
DELIMITER :3

select media_moeda(2)
