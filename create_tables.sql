CREATE TABLE PROFESSOR(
    PID INTEGER NOT NULL,
    PNAME VARCHAR(20) NOT NULL,
    DEPARTMENT_ID INTEGER, NOT NULL,
    SALARY INTEGER NOT NULL,
    EMAIL VARCHAR(20) NOT NULL,
    TENURE DATE NOT NULL
);

CREATE TABLE PROFESSOR(
    PID INTEGER NOT NULL,
    PNAME VARCHAR(20) NOT NULL,
    DEPARTMENT_ID INTEGER, NOT NULL,
    SALARY INTEGER NOT NULL,
    EMAIL VARCHAR(20) NOT NULL,
    TENURE DATE NOT NULL
);

CREATE TABLE SECTION(
    SECTION_ID INTEGER NOT NULL,
    COURSE_ID INTEGER NOT NULL,
    TERM VARCHAR(10) NOT NULL,
    PROFFESOR_ID INTEGER NOT NULL,
    SECTION_NUMBER INTEGER NOT NULL
);

CREATE TABLE PROFESSOR(
    UID VARCHAR(4) NOT NULL;
    SECTION_ID INT NOT NULL;
);

CREATE TABLE COURSE(
    COURSE_ID INTEGER NOT NULL;
    COURSE_NAME INTEGER NOT NULL;
    COURSE_DESC VARCHAR(500) NOT NULL;
    CREDITS INTEGER NOT NULL;
);

CREATE TABLE DEPARTMENT(
    DEPARTMENT_ID INTEGER NOT NULL,
    DEPARTMENT_NAME VARCHAR(20) NOT NULL,
    YEAR_FOUNDED DATE NOT NULL,
    BUDGET FLOAT NOT NULL,
    DEPARTMENT_CHAIR VARCHAR(20) NOT NULL,
);

CREATE TABLE STUDENTS(
    UID VARCHAR(4) NOT NULL,
    FIRST_NAME VARCHAR(15) NOT NULL,
    LAST_NAME VARCHAR(15) NOT NULL,
    DATE_OF_BIRTH DATE NOT NULL,
    GPA FLOAT NOT NULL,
    MAJOR_ID INTEGER NOT NULL,
    EMAIL VARCHAR(20) NOT NULL,
    UNDERGRADUATE BOOLEAN NOT NULL,
    CLASS_STANDING VARCHAR(10) NOT NULL,
    PASSWORD VARCHAR(15) NOT NULL,
    PHONE VARCHAR(10) NOT NULL,
    ADDRESS VARCHAR(20) NOT NULL
);

