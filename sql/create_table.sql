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

CREATE TABLE ba_raid (
	raid_id             VARCHAR2(10) NOT NULL,
    name                VARCHAR2(200) NOT NULL,
    status              VARCHAR2(20) NOT NULL,
    CONSTRAINT raid_id_pk PRIMARY KEY (raid_id)
);

CREATE TABLE dev_ba_raid (
	raid_id             VARCHAR2(10) NOT NULL,
    name                VARCHAR2(200) NOT NULL,
    status              VARCHAR2(20) NOT NULL,
    CONSTRAINT dev_raid_id_pk PRIMARY KEY (raid_id)
);

CREATE TABLE ba_raid_score (
	raid_id             VARCHAR2(10) NOT NULL,
    user_id             VARCHAR2(20) NOT NULL,
    score               NUMBER(10) NOT NULL,
    torment_rank        NUMBER(10) NOT NULL,
    final_rank          NUMBER(10) NOT NULL,
    party_data          VARCHAR2(32767) NOT NULL,
    CONSTRAINT ensure_json CHECK (party_data IS JSON)
);

CREATE TABLE dev_ba_raid_score (
	raid_id             VARCHAR2(10) NOT NULL,
    user_id             VARCHAR2(20) NOT NULL,
    score               NUMBER(10) NOT NULL,
    torment_rank        NUMBER(10) NOT NULL,
    final_rank          NUMBER(10) NOT NULL,
    party_data          VARCHAR2(32767) NOT NULL,
    CONSTRAINT dev_ensure_json CHECK (party_data IS JSON)
);

CREATE TABLE ba_named_user (
    user_id                 VARCHAR2(20) NOT NULL,
    youtube_url         VARCHAR2(200) NOT NULL,
    name                VARCHAR2(50) NOT NULL,
    description         VARCHAR2(200) NOT NULL,
    CONSTRAINT uid_pk PRIMARY KEY (user_id)
);