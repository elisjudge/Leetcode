CREATE TABLE IF NOT EXISTS Teacher (
    teacher_id INTEGER NOT NULL,
    subject_id INTEGER NOT NULL,
    dept_id INTEGER NOT NULL
);

DELETE FROM Teacher;

INSERT INTO Teacher (teacher_id, subject_id, dept_id) VALUES (1, 2, 3);
INSERT INTO Teacher (teacher_id, subject_id, dept_id) VALUES (1, 2, 4);
INSERT INTO Teacher (teacher_id, subject_id, dept_id) VALUES (1, 3, 3);
INSERT INTO Teacher (teacher_id, subject_id, dept_id) VALUES (2, 1, 1);
INSERT INTO Teacher (teacher_id, subject_id, dept_id) VALUES (2, 2, 1);
INSERT INTO Teacher (teacher_id, subject_id, dept_id) VALUES (2, 3, 1);
INSERT INTO Teacher (teacher_id, subject_id, dept_id) VALUES (2, 4, 1);
