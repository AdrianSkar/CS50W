SELECT
	fp.id AS pass_id,
	fp.first,
	fp.last,
	ff.duration AS ff_duration,
	fa.code AS origin_code,
	fa.city AS origin_city,
	fad.code AS destination_code,
	fad.city AS destination_city
FROM
	flights_passenger AS fp
	JOIN flights_passenger_flights AS fpf ON fp.id = fpf.passenger_id
	JOIN flights_flight AS ff ON ff.id = fpf.flight_id
	JOIN flights_airport AS fa ON fa.id = ff.origin_id
	JOIN flights_airport AS fad ON fad.id = ff.destination_id;