-------------------------
-- Section 03, Lesson 01
-------------------------

------
--  SELECT statements
------


-- SELECT with all columns listed
SELECT MAKE, MODEL, MODEL_YEAR, MILEAGE, COLOR, PRICE, CONDITION_CD FROM LOT_CARS;

-- SELECT with ASTERISK in place for all columns
SELECT * FROM LOT_CARS;


-------------------------
-- Section 03, Lesson 02
-------------------------

------
--  WHERE clauses
------


-- WHERE clause returning only Ford vehicles
SELECT * FROM LOT_CARS
 WHERE MAKE = 'Ford'
;

-- WHERE clause returning only Red Ford vehicles
SELECT * FROM LOT_CARS
 WHERE MAKE = 'Ford'
    OR COLOR = 'Red'
;

-- All Ford vehicles and all Red Toyota vehicles
SELECT * FROM LOT_CARS
 WHERE MAKE = 'Ford'
   OR (COLOR = 'Red'
         AND MAKE = 'Toyota'
      )
;

-- All cars except Fords:
SELECT * FROM LOT_CARS
 WHERE MAKE <> 'Ford'
;

-- All cars whose price is greater or equal to 10,000 dollars
SELECT * FROM LOT_CARS
 WHERE PRICE >= 10000
;



-------------------------
-- Section 03, Lesson 03
-------------------------

------
--  ORDER BY
------


-- SELECT statement with simple order by
SELECT MAKE, MODEL_YEAR, PRICE
FROM LOT_CARS
ORDER BY MAKE
;

-- Sorting on multiple columns
SELECT MAKE, MODEL_YEAR, PRICE
FROM LOT_CARS
ORDER BY MAKE, MODEL_YEAR
;

-- Descending Order sorting
SELECT MAKE, MODEL_YEAR, PRICE
FROM LOT_CARS
ORDER BY MAKE, MODEL_YEAR DESC
;

-- ORDER BY using column position instead of column name
SELECT MAKE, MODEL_YEAR, PRICE
FROM LOT_CARS
ORDER BY 1, 2 DESC
;



-------------------------
-- Section 03, Lesson 04
-------------------------

------
--  JOINS
------


-- Common structure of a non-ANSI join
-- of two tables with table aliases
SELECT 
  LT.MAKE, 
  LT.MODEL, 
  LT.CONDITION_CD,
  CT.DESCRIPTION
FROM LOT_CARS LT,
     CONDITION_TBL CT
WHERE LT.CONDITION_CD = CT.CONDITION_CD
;

-- Structure of an ANSI join of two tables
-- using INNER JOIN keyword. Note that without
-- the word INNER, the INNER is implied.
SELECT
  LT.MAKE, 
  LT.MODEL, 
  LT.MODEL_YEAR,
  LT.COLOR,
  LT.CONDITION_CD,
  CT.DESCRIPTION
FROM LOT_CARS LT INNER JOIN CONDITION_TBL CT ON LT.CONDITION_CD = CT.CONDITION_CD
WHERE LT.MAKE = 'Ford'
ORDER BY LT.MAKE, LT.MODEL_YEAR DESC
;

-- Natural Join when the joined columns in each table
-- have the same column name
SELECT
  MAKE, 
  MODEL, 
  MODEL_YEAR,
  COLOR,
  CONDITION_CD,
  DESCRIPTION
FROM LOT_CARS NATURAL JOIN CONDITION_TBL
WHERE MAKE = 'Ford'
ORDER BY MAKE, MODEL_YEAR DESC
;


-------------------------
-- Section 03, Lesson 05
-------------------------

------
--  GROUP BY
------


-- Return the number of vehicles within each make and model year
-- sorted by Make and Model Year
SELECT MAKE, MODEL_YEAR, COUNT(*) 
FROM LOT_CARS
GROUP BY MAKE, MODEL_YEAR
ORDER BY MAKE, MODEL_YEAR
;

-- Count vehicles by MAKE, but only show those 
-- makes that have more than 2 vehicles
SELECT MAKE, COUNT(*) AS QUANTITY
FROM LOT_CARS
GROUP BY MAKE
HAVING COUNT(*) > 2
ORDER BY MAKE
;

-- List the make of vehicles that only
-- have one vehicle of that make on the lot
-- and label the column QUANTITY
SELECT MAKE, COUNT(*) AS QUANTITY 
FROM LOT_CARS
GROUP BY MAKE
HAVING COUNT(*) = 1
ORDER BY MAKE
;

-- Same query, but removing the redundant
-- COUNT(*) column from the SELECT columns
SELECT MAKE
FROM LOT_CARS
GROUP BY MAKE
HAVING COUNT(*) = 1
ORDER BY MAKE
;



-------------------------
-- Section 03, Lesson 06
-------------------------

------
--  Aggregate Functions


-- Count all rows in the table
SELECT COUNT(*) FROM LOT_CARS;

-- Count all values in a table column
-- Note that this will not count
-- rows with a null in the CONDITION_CD column
SELECT COUNT(CONDITION_CD) FROM LOT_CARS;

-- Count all distinct values in the MALE column
SELECT COUNT(DISTINCT MAKE) FROM LOT_CARS;

-- COUNT function, grouping by joined table columns
-- and a column alias (QUANTITY) - Non-ANSI
SELECT LT.MAKE, CT.DESCRIPTION, COUNT(*) AS QUANTITY 
  FROM LOT_CARS LT, 
       CONDITION_TBL CT
WHERE LT.CONDITION_CD = CT.CONDITION_CD
GROUP BY LT.MAKE, CT.DESCRIPTION
ORDER BY LT.MAKE
;

-- COUNT function, grouping by joined table columns
-- and a column alias (QUANTITY) - ANSI Natural Join
SELECT MAKE, DESCRIPTION, COUNT(*) AS QUANTITY 
  FROM LOT_CARS NATURAL JOIN CONDITION_TBL
GROUP BY MAKE, DESCRIPTION
ORDER BY MAKE
;

-- Minimum PRICE by MAKE
SELECT MAKE, MIN(PRICE)
  FROM LOT_CARS
GROUP BY MAKE
ORDER BY MAKE
;

-- Maximum PRICE by MAKE
SELECT MAKE, MAX(PRICE)
 FROM LOT_CARS
GROUP BY MAKE
ORDER BY MAKE
;

-- Average PRICE across each MAKE
SELECT MAKE, AVG(PRICE)
 FROM LOT_CARS
GROUP BY MAKE
ORDER BY MAKE
;

-- Total MILEAGE by MAKE
SELECT MAKE, SUM(MILEAGE)
 FROM LOT_CARS
GROUP BY MAKE
ORDER BY MAKE
;

-- Multiple functions 
SELECT MAKE, MIN(PRICE),  MAX(PRICE), AVG(PRICE), SUM(MILEAGE)
 FROM LOT_CARS
GROUP BY MAKE
ORDER BY MAKE
;



-------------------------
-- Section 03, Lesson 07
-------------------------

------
--  String Functions
------


-- Concatenate two fields (Oracle Specific)
SELECT MAKE || MODEL
FROM LOT_CARS
;

-- Concatenate with separation (Oracle Specific) 
SELECT MAKE || ' ' || MODEL
FROM LOT_CARS
;

-- Concatenate using standard CONCAT function


-- Change column values to all UPPER CASE
SELECT UPPER(MAKE)
FROM LOT_CARS
;

-- Comparison with UPPER 
SELECT *
FROM LOT_CARS
WHERE UPPER(MAKE) = 'NISSAN'
;


-- Change column values to all LOWER CASE
SELECT LOWER(MAKE)
FROM LOT_CARS
;

-- Replace characters within a string
SELECT MODEL, REPLACE(MODEL, 'c', 'x')
FROM LOT_CARS
;

-- Length of a string
SELECT MODEL, LENGTH(MODEL)
FROM LOT_CARS
;

-- Substring first three characters
SELECT MODEL, SUBSTR(MODEL, 1, 3)
FROM LOT_CARS
;


-- Omitting third parameter assumes end of string
SELECT MODEL, SUBSTR(MODEL, 2)
FROM LOT_CARS
;

-- Start from end of string (right-most character)
SELECT MODEL, SUBSTR(MODEL, -1)
FROM LOT_CARS
;

-- Left-most character
SELECT MODEL, SUBSTR(MODEL, 1, 1)
FROM LOT_CARS
;

-- Combined functions (Full string less first and last character)
SELECT MODEL, SUBSTR(MODEL, 2, LENGTH(MODEL) - 2)
FROM LOT_CARS
;

-- Reverse a string
SELECT MODEL, REVERSE(MODEL)
FROM LOT_CARS
;

-- Default value when null
SELECT MAKE, MODEL, NVL(CONDITION_CD, 2)
FROM LOT_CARS
;

-- Joining tables with an NVL column
SELECT 
  LC.MAKE, 
  LC.MODEL, 
  CT.DESCRIPTION
FROM LOT_CARS LC,
     CONDITION_TBL CT
WHERE NVL(LC.CONDITION_CD, 2) = CT.CONDITION_CD
;



-------------------------
-- Section 03, Lesson 08
-------------------------

------
--  Numeric Functions
------

-- Square Root
SELECT SQRT(3600) FROM DUAL;

-- 3 to the 2nd power (3 squared)
SELECT POWER(3, 2) FROM DUAL;

-- Standard math expressions
SELECT 5 * ( 4 + 2) FROM DUAL;

-- Absolute Value
SELECT ABS(-23) FROM DUAL;

-- Round to 2 decimal places
SELECT ROUND(125.1286,2) FROM DUAL;

-- Round to the nearest thousand
SELECT ROUND(12545, -3) FROM DUAL;

-- Integer portion of a number (No rounding)
SELECT TRUNC(12345.999) FROM DUAL;

-- Convert number to string
SELECT 12345, TO_CHAR(12345) FROM DUAL;

-- Combined Functions
SELECT TO_CHAR(SQRT(ROUND(ABS(ROUND(-643498.348373,2)),-4) / 10000)) FROM DUAL;

-- 10% Discounted Price
SELECT MAKE, MODEL, PRICE, PRICE - (PRICE * .1) AS DISCOUNT
FROM LOT_CARS;

-- Display price as nnK (ie, 11984 -> 12K)
SELECT MAKE, MODEL, PRICE, TO_CHAR(ROUND(PRICE,-3) / 1000) || 'K' AS PRICE_IN_K
FROM LOT_CARS;



-------------------------
-- Section 03, Lesson 09
-------------------------

------
--  Date Functions
------



-- Get Current Date
SELECT SYSDATE FROM DUAL;

-- Get Current Date / Time
SELECT SYSTIMESTAMP FROM DUAL;

-- Get Day (Full Text)
SELECT SYSDATE, TO_CHAR(SYSDATE, 'DAY') FROM DUAL;

-- Get Day (Full text - Mixed Case)
SELECT SYSDATE, TO_CHAR(SYSDATE, 'Day') FROM DUAL;

-- Get Day (Abbreviation)
SELECT SYSDATE, TO_CHAR(SYSDATE, 'DY') FROM DUAL;

-- Get Day (Abbreviation - Mixed Case)
SELECT SYSDATE, TO_CHAR(SYSDATE, 'Dy') FROM DUAL;

-- Day of the Month
SELECT TO_CHAR(SYSDATE, 'DD') FROM DUAL;

-- Day of the Year
SELECT TO_CHAR(SYSDATE, 'DDD') FROM DUAL;

-- Get Month (Full Text)
SELECT TO_CHAR(SYSDATE, 'MONTH') FROM DUAL;

-- Get Month (Full Text - Mixed Case)
SELECT TO_CHAR(SYSDATE, 'Month') FROM DUAL;

 -- Get Month (Abbreviation)
SELECT TO_CHAR(SYSDATE, 'MON') FROM DUAL;

-- Get Month (Full Text - Mixed Case)
SELECT TO_CHAR(SYSDATE, 'Mon') FROM DUAL;

-- 2 Digit Month
SELECT TO_CHAR(SYSDATE, 'MM') FROM DUAL;

-- Get 4 Digit Year
SELECT TO_CHAR(SYSDATE, 'YYYY') FROM DUAL;

-- Get 3 Digit Year
SELECT TO_CHAR(SYSDATE, 'YYY') FROM DUAL;

-- Get 2 Digit Year
SELECT TO_CHAR(SYSDATE, 'YY') FROM DUAL;

-- Get 1 Digit Year
SELECT TO_CHAR(SYSDATE, 'Y') FROM DUAL;

-- Full Text Year
SELECT TO_CHAR(SYSDATE, 'Year') FROM DUAL;

-- Formatted Full Date (Long Form)
SELECT TO_CHAR(SYSDATE, 'DL') FROM DUAL;

-- Formatted Full Date (Short Form)
SELECT TO_CHAR(SYSDATE, 'DS') FROM DUAL;

-- TO_CHAR with various Format Models
SELECT TO_CHAR(SYSDATE, 'YYYY-MM-DD') FROM DUAL;
SELECT TO_CHAR(SYSDATE, 'Dy, Mon DD, YYYY') FROM DUAL;
SELECT TO_CHAR(SYSTIMESTAMP, 'Dy, Mon DD, YYYY') FROM DUAL;

-- Time Stamps
-- Hours from Timestamp (12 hour clock)
SELECT TO_CHAR(SYSTIMESTAMP, 'HH') FROM DUAL;
SELECT TO_CHAR(SYSTIMESTAMP, 'HH12') FROM DUAL;

-- Hours from Timestamp (24 hour clock)
SELECT TO_CHAR(SYSTIMESTAMP, 'HH24') FROM DUAL;

-- Minutes from a Timestamp
SELECT TO_CHAR(SYSTIMESTAMP, 'MI') FROM DUAL;

-- Seconds from a Timestamp
SELECT TO_CHAR(SYSTIMESTAMP, 'SS') FROM DUAL;

-- AM/PM (Both return identical results)
SELECT TO_CHAR(SYSTIMESTAMP, 'AM') FROM DUAL;
SELECT TO_CHAR(SYSTIMESTAMP, 'PM') FROM DUAL;

-- Fractional Seconds from a Timestamp
SELECT TO_CHAR(SYSTIMESTAMP, 'FF') FROM DUAL;

-- Fractional Seconds from a Timestamp - 2 positions
SELECT TO_CHAR(SYSTIMESTAMP, 'FF2') FROM DUAL;

-- Formatted time
SELECT TO_CHAR(SYSTIMESTAMP, 'HH:MI:SS.FF1 AM') FROM DUAL;

-- Formatted Date and Time 
SELECT TO_CHAR(SYSTIMESTAMP, 'Dy, Mon DD, YYYY HH:MI:SS.FF1 AM') FROM DUAL;

--- Date Arithmetic
-- Add one day (Tomorrow)
SELECT TO_CHAR(SYSDATE + 1, 'Dy, Mon DD, YYYY') FROM DUAL;

-- Subtract 1 Day (Yesterday)
SELECT TO_CHAR(SYSDATE - 1, 'Dy, Mon DD, YYYY') FROM DUAL;

-- Add 7 Days (Next Week)_
SELECT TO_CHAR(SYSDATE + 7, 'Dy, Mon DD, YYYY') FROM DUAL;

-- Add a Month to Today
SELECT TO_CHAR(ADD_MONTHS(SYSDATE, 1), 'Dy, Mon DD, YYYY') FROM DUAL;

-- Add a Year to Today
SELECT TO_CHAR(ADD_MONTHS(SYSDATE, 12), 'Dy, Mon DD, YYYY') FROM DUAL;

-- String to Date
SELECT TO_DATE('Dec 14, 2015', 'Mon DD, YYYY') FROM DUAL;
SELECT TO_DATE('2015-12-14', 'YYYY-MM-DD') FROM DUAL;



-------------------------
-- Section 04, Lesson 01
-------------------------

------
--  IN CONDITION Subqueries
------

-- In Subquery
SELECT *
FROM LOT_CARS
WHERE CONDITION_CD IN 
(
   SELECT CONDITION_CD
      FROM CONDITION_TBL
  WHERE UPPER(DESCRIPTION) LIKE '%O%'
)
;

-- Not In Subquery
SELECT *
FROM LOT_CARS
WHERE CONDITION_CD NOT IN 
(
   SELECT CONDITION_CD
      FROM CONDITION_TBL
  WHERE UPPER(DESCRIPTION) LIKE '%O%'
)
;

-- In List
SELECT *
FROM LOT_CARS
WHERE UPPER(COLOR) IN ('RED', 'BLUE')
;

 -- Not In List
SELECT *
FROM LOT_CARS
WHERE UPPER(COLOR) NOT IN ('RED', 'BLUE')
;



-------------------------
-- Section 04, Lesson 02
-------------------------

---
-- Uncorrelated Subquery
---
SELECT COLOR, COUNT(*) 
  FROM LOT_CARS
 GROUP BY COLOR
HAVING COUNT(*) = (
          SELECT MAX(COUNT(*)) 
           FROM LOT_CARS
          GROUP BY COLOR
        )
;



-------------------------
-- Section 04, Lesson 03
-------------------------

--- 
-- Correlated SubQuery
---
SELECT *
FROM LOT_CARS LC
WHERE PRICE > (
    SELECT AVG(PRICE) FROM LOT_CARS LC2
     WHERE LC2.MAKE = LC.MAKE
)
;



-------------------------
-- Section 04, Lesson 04
-------------------------

---
-- Exists Condition Subqueries
---

-- Exists
SELECT *
FROM LOT_CARS LC
WHERE  EXISTS
(
  SELECT 'X'
  FROM CONDITION_TBL CT
  WHERE CT.CONDITION_CD = LC.CONDITION_CD
)
;


-- Not Exists
SELECT *
FROM LOT_CARS LC
WHERE NOT EXISTS
(
  SELECT 'X'
  FROM CONDITION_TBL CT
  WHERE CT.CONDITION_CD = LC.CONDITION_CD
)
;



-------------------------
-- Section 06, Lesson 02
-------------------------

---
-- Individual SQL statements for each table
---
SELECT VIN, MAKE, MODEL FROM LOT_CARS;

SELECT VIN, MAKE, MODEL FROM RENT_CARS;

---
-- Union both queries to form a single result set
---
SELECT VIN, MAKE, MODEL FROM LOT_CARS
UNION 
SELECT VIN, MAKE, MODEL FROM RENT_CARS;

---
-- Error resulting from unmatched columns (4 in top, 3 in bottom)
---
SELECT VIN, MAKE, MODEL, MODEL_YEAR FROM LOT_CARS
UNION 
SELECT VIN, MAKE, MODEL FROM RENT_CARS;


---
-- Valid Union with different columns, but the same 
-- column type (MODEL_YEAR, MILEAGE)
---
SELECT VIN, MAKE, MODEL, MODEL_YEAR FROM LOT_CARS
UNION 
SELECT VIN, MAKE, MODEL, MILEAGE FROM RENT_CARS;


---
-- Error resulting from mismatched column types, 
-- MODEL_YEAR (Numeric) on top, STATE (String) on bottom
---
SELECT VIN, MAKE, MODEL, MODEL_YEAR FROM LOT_CARS
UNION 
SELECT VIN, MAKE, MODEL, STATE FROM RENT_CARS;


---
-- Union will remove duplicate result rows
---
SELECT MAKE, MODEL FROM LOT_CARS
UNION 
SELECT MAKE, MODEL FROM RENT_CARS;

---
-- Union All will retain duplicate result rows
---
SELECT MAKE, MODEL FROM LOT_CARS
UNION ALL
SELECT MAKE, MODEL FROM RENT_CARS;



-------------------------
-- Section 06, Lesson 03
-------------------------

---
-- Inner join of RENT_CARS and RENTALS where VINs match
---
SELECT RC.VIN, 
       RC.MAKE, 
       RC.MODEL, 
       RC.MODEL_YEAR, 
       RC.MILEAGE, 
       RC.STATE, 
       RC.TAG, 
       RC.IN_OUT, 
       R.RENTAL_ID, 
       R.DT_OUT, 
       R.DT_RETURN
FROM RENT_CARS RC, 
     RENTALS R
WHERE RC.VIN = R.VIN
;
 
---
-- Left Outer Join 
---
SELECT RC.VIN, 
       RC.MAKE, 
       RC.MODEL, 
       RC.MODEL_YEAR, 
       RC.MILEAGE, 
       RC.STATE, 
       RC.TAG, 
       RC.IN_OUT, 
       R.RENTAL_ID, 
       R.DT_OUT, 
       R.DT_RETURN
FROM RENT_CARS RC LEFT OUTER JOIN  RENTALS R ON RC.VIN = R.VIN
;


---
-- Correlated Subquery returns max DT_OUT for each VIN
---
SELECT R.VIN, R.RENTAL_ID, R.DT_OUT, R.DT_RETURN
FROM RENTALS R 
WHERE R.DT_OUT = (
                 SELECT MAX(R_DT.DT_OUT)
                  FROM RENTALS R_DT
                 WHERE R.VIN = R_DT.VIN
                )
;



---
-- Using a query as a table with a table alias
---
SELECT RQ.VIN, RQ.RENTAL_ID, RQ.DT_OUT, RQ.DT_RETURN FROM 
(
  SELECT R.VIN, R.RENTAL_ID, R.DT_OUT, R.DT_RETURN
  FROM RENTALS R 
  WHERE R.DT_OUT = (
                   SELECT MAX(R_DT.DT_OUT)
                    FROM RENTALS R_DT
                   WHERE R.VIN = R_DT.VIN
                  )
) RQ
;

---
-- Left Outer Join using query as Right "table"
---
SELECT RC.VIN, 
       RC.MAKE, 
       RC.MODEL, 
       RC.MODEL_YEAR, 
       RC.MILEAGE, 
       RC.STATE, 
       RC.TAG, 
       RC.IN_OUT, 
       RQ.RENTAL_ID, 
       RQ.DT_OUT, 
       RQ.DT_RETURN
FROM RENT_CARS RC LEFT OUTER JOIN 
    (
      SELECT R.VIN, R.RENTAL_ID, R.DT_OUT, R.DT_RETURN
      FROM RENTALS R 
      WHERE R.DT_OUT = (
                       SELECT MAX(R_DT.DT_OUT)
                        FROM RENTALS R_DT
                       WHERE R.VIN = R_DT.VIN
                      )
    ) RQ ON RC.VIN = RQ.VIN
;



-------------------------
-- Section 06, Lesson 04
-------------------------

---
-- Cross Join, or Cartesian Join of two tables
---
SELECT *
FROM RENT_CARS CROSS JOIN RENTALS
;

---
-- Getting the number of rows in the table to the
-- power of 3: 30**3 = 27,000 Rows
---
SELECT *
FROM LOT_CARS CROSS JOIN LOT_CARS CROSS JOIN LOT_CARS 
;



-------------------------
-- Section 07, Lesson 01
-------------------------

---
-- Simple Update
---
UPDATE RENT_CARS
SET STATE = 'UT', TAG = 'XX-0987'
WHERE VIN = 'YLWDMZU5DWMHAMUR5'
;

---
-- Update with Correlated Subquery
---
UPDATE RENT_CARS RC
SET RC.IN_OUT = 'O'
WHERE EXISTS
(SELECT 'X'
  FROM RENTALS R
 WHERE RC.VIN = R.VIN
   AND R.DT_RETURN > TO_DATE('2017-04-15', 'YYYY-MM-DD')
 )
;

---
-- Update with check not to update to same value
--- 
UPDATE RENT_CARS RC
SET RC.IN_OUT = 'O'
WHERE EXISTS
(SELECT 'X'
  FROM RENTALS R
 WHERE RC.VIN = R.VIN
   AND R.DT_RETURN > TO_DATE('2017-04-15', 'YYYY-MM-DD')
 )
AND RC.IN_OUT <> 'O'
;



-------------------------
-- Section 07, Lesson 02
-------------------------

---
-- Simple Delete
---
DELETE FROM RENT_CARS
WHERE VIN = 'YLWDMZU5DWMHAMUR5'
;

---
-- Delete with correlated subquery
---
DELETE FROM RENT_CARS RC
WHERE NOT EXISTS (
  SELECT 'X'
    FROM RENTALS R
  WHERE RC.VIN = R.VIN
  )
;



-------------------------
-- Section 07, Lesson 03
-------------------------

---
-- Basic Insert with Values
---
INSERT INTO LOT_CARS (VIN, MAKE, MODEL, MODEL_YEAR, MILEAGE, COLOR, PRICE, CONDITION_CD) 
VALUES
('XXXXX7777733333II', 'Honda', 'Accord', 2017, 876, 'Red', 22938, 3)
;

---
-- Insert from a select of another table
---
INSERT INTO LOT_CARS_COPY
(VIN, MAKE, MODEL, MODEL_YEAR, MILEAGE, COLOR, PRICE, CONDITION_CD)
SELECT VIN, MAKE, MODEL, MODEL_YEAR, MILEAGE, COLOR, PRICE, CONDITION_CD 
FROM LOT_CARS
;


---
--Insert from a select of another table (Short Form)
---
INSERT INTO LOT_CARS_COPY
SELECT * FROM LOT_CARS
;

---
-- Cross Join to insert large volume of data
--- 
INSERT INTO LOT_CARS_COPY
SELECT LC1.* FROM LOT_CARS LC1 CROSS JOIN LOT_CARS LC2 CROSS JOIN LOT_CARS LC3
;



