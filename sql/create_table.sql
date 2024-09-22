CREATE TABLE ba_students (
	student_id          NUMBER(10)	NOT NULL,
    name                VARCHAR2(50) NOT NULL,
    CONSTRAINT student_id_pk PRIMARY KEY (student_id)
);

CREATE TABLE dev_ba_students (
	student_id          NUMBER(10)	NOT NULL,
    name                VARCHAR2(50) NOT NULL,
    CONSTRAINT dev_student_id_pk PRIMARY KEY (student_id)
);