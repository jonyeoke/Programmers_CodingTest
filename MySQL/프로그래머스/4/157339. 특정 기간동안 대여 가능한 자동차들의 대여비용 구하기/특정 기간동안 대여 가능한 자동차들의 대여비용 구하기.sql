SELECT
    c.car_id,
    c.car_type,
    c.daily_fee * 30 * (100 - p.discount_rate) / 100 AS fee
FROM CAR_RENTAL_COMPANY_CAR c
JOIN CAR_RENTAL_COMPANY_DISCOUNT_PLAN p
    ON c.car_type = p.car_type
WHERE c.car_type IN ('세단', 'SUV')
  AND c.car_id NOT IN (
      SELECT car_id
      FROM CAR_RENTAL_COMPANY_RENTAL_HISTORY
      WHERE end_date >= '2022-11-01'
        AND start_date <= '2022-11-30'
  )
  AND p.duration_type = '30일 이상'
  AND c.daily_fee * 30 * (100 - p.discount_rate) / 100 >= 500000
  AND c.daily_fee * 30 * (100 - p.discount_rate) / 100 < 2000000
ORDER BY
    fee DESC,
    c.car_type ASC,
    c.car_id DESC;