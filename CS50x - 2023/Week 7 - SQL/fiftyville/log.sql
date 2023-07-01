-- retrieve description of crime report
SELECT description
FROM crime_scene_reports
WHERE month = 7 AND day = 28 AND street = 'Humphrey Street';

--get interview transcripts frm witnesses
SELECT transcript
FROM interviews
WHERE month = 7 AND day = 28;

--Check passengers using passport numbers of callers
SELECT passport_number
FROM passengers
WHERE passport_number IN
    (
    SELECT passport_number
    FROM people
    WHERE phone_number IN
        --check phone callers using those phone number
        (
        SELECT caller
        FROM phone_calls
        WHERE caller IN
        (
            --get phone number of the car owners left bakery at that time
            SELECT phone_number
            FROM people
            JOIN bakery_security_logs people.license_plate = bakery_security_logs.license_plate
            WHERE month = 7 AND day = 28 AND hour = 10 AND minute > 15 AND minute < 25
        )
        AND month = 7 AND day = 28 AND duration < 70)

    )
    AND flight_id IN
    (
        ---earliest flight id out of Fiftyville the nextday
        SELECT id
        FROM flights
        WHERE origin_airport_id =
        (
            SELECT id
            FROM airports
            WHERE city = 'Fiftyville'
        )
        AND month = 7 AND day = 29 AND hour < 9
    );

--get thief name who owns the car, get mpney from atm and flys next day
SELECT name
FROM people
WHERE passport_number IN
        (
            SELECT passport_number
            FROM passengers
            WHERE passport_number IN
                (
                SELECT passport_number
                FROM people
                WHERE phone_number IN
                    (
                    SELECT caller
                    FROM phone_calls
                    WHERE caller IN
                    (
                        SELECT phone_number
                        FROM people
                        WHERE license_plate IN
                        (
                            SELECT license_plate
                            FROM bakery_security_logs
                            WHERE month = 7 AND day = 28 AND hour = 10 AND minute > 15 AND minute < 25
                        )
                    )
                    AND month = 7 AND day = 28 AND duration < 70)

                )
                AND flight_id IN
                (
                    SELECT id
                    FROM flights
                    WHERE origin_airport_id =
                    (
                        SELECT id
                        FROM airports
                        WHERE city = 'Fiftyville'
                    )
                    AND month = 7 AND day = 29 AND hour < 9
                )
        )
AND phone_number IN
    (
        SELECT caller
        FROM phone_calls
        WHERE caller IN
        (
            SELECT phone_number
            FROM people
            WHERE license_plate IN
            (
                SELECT license_plate
                FROM bakery_security_logs
                WHERE month = 7 AND day = 28 AND hour = 10 AND minute > 15 AND minute < 25
            )
        )
        AND month = 7 AND day = 28 AND duration < 60
    )
AND id IN
    (
        SELECT person_id
        FROM bank_accounts
        WHERE account_number IN
        (
            SELECT account_number
            FROM atm_transactions
            WHERE month = 7 AND day = 28
        )
    );

--The accomplices
SELECT name
FROM people
WHERE phone_number IN
(
    SELECT receiver
    FROM phone_calls
    WHERE caller =
    (
        SELECT phone_number
        FROM people
        WHERE name =
        (
            SELECT name
FROM people
WHERE passport_number IN
        (
            SELECT passport_number
            FROM passengers
            WHERE passport_number IN
                (
                SELECT passport_number
                FROM people
                WHERE phone_number IN
                    (
                    SELECT caller
                    FROM phone_calls
                    WHERE caller IN
                    (
                        SELECT phone_number
                        FROM people
                        WHERE license_plate IN
                        (
                            SELECT license_plate
                            FROM bakery_security_logs
                            WHERE month = 7 AND day = 28 AND hour = 10 AND minute > 15 AND minute < 25
                        )
                    )
                    AND month = 7 AND day = 28 AND duration < 70)

                )
                AND flight_id IN
                (
                    SELECT id
                    FROM flights
                    WHERE origin_airport_id =
                    (
                        SELECT id
                        FROM airports
                        WHERE city = 'Fiftyville'
                    )
                    AND month = 7 AND day = 29 AND hour < 9
                )
        )
AND phone_number IN
    (
        SELECT caller
        FROM phone_calls
        WHERE caller IN
        (
            SELECT phone_number
            FROM people
            WHERE license_plate IN
            (
                SELECT license_plate
                FROM bakery_security_logs
                WHERE month = 7 AND day = 28 AND hour = 10 AND minute > 15 AND minute < 25
            )
        )
        AND month = 7 AND day = 28 AND duration < 60
    )
AND id IN
    (
        SELECT person_id
        FROM bank_accounts
        WHERE account_number IN
        (
            SELECT account_number
            FROM atm_transactions
            WHERE month = 7 AND day = 28
        )
    )
        )
    )
AND month = 7 AND day = 28 AND duration < 60
)

;

--destination_airport
SELECT city
FROM airports
WHERE id =
    (SELECT destination_airport_id
    FROM flights
    WHERE origin_airport_id =
    (
        SELECT id
        FROM airports
        WHERE city = "Fiftyville"
    )
    AND month = 7 AND day = 29 AND hour < 9
    )
    ;