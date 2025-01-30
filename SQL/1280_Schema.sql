CREATE TABLE IF NOT EXISTS Students (
    student_id INTEGER PRIMARY KEY,
    student_name VARCHAR(20)
);

CREATE TABLE IF NOT EXISTS Subjects (
    subject_name VARCHAR(20) PRIMARY KEY
);

CREATE TABLE IF NOT EXISTS Examinations (
    exam_id INTEGER PRIMARY KEY AUTOINCREMENT,
    student_id INTEGER,
    subject_name VARCHAR(20),
    FOREIGN KEY (student_id) REFERENCES Students(student_id),
    FOREIGN KEY (subject_name) REFERENCES Subjects(subject_name)
);

INSERT INTO Students (student_id, student_name) VALUES (1, 'Alice');
INSERT INTO Students (student_id, student_name) VALUES (2, 'Bob');
INSERT INTO Students (student_id, student_name) VALUES (13, 'John');
INSERT INTO Students (student_id, student_name) VALUES (6, 'Alex');

INSERT INTO Subjects (subject_name) VALUES ('Math');
INSERT INTO Subjects (subject_name) VALUES ('Physics');
INSERT INTO Subjects (subject_name) VALUES ('Programming');

INSERT INTO Examinations (student_id, subject_name) VALUES (1, 'Math');
INSERT INTO Examinations (student_id, subject_name) VALUES (1, 'Physics');
INSERT INTO Examinations (student_id, subject_name) VALUES (1, 'Programming');
INSERT INTO Examinations (student_id, subject_name) VALUES (2, 'Programming');
INSERT INTO Examinations (student_id, subject_name) VALUES (1, 'Physics');
INSERT INTO Examinations (student_id, subject_name) VALUES (1, 'Math');
INSERT INTO Examinations (student_id, subject_name) VALUES (13, 'Math');
INSERT INTO Examinations (student_id, subject_name) VALUES (13, 'Programming');
INSERT INTO Examinations (student_id, subject_name) VALUES (13, 'Physics');
INSERT INTO Examinations (student_id, subject_name) VALUES (2, 'Math');
INSERT INTO Examinations (student_id, subject_name) VALUES (1, 'Math');
