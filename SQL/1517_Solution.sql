SELECT
    user_id,
    name,
    mail
FROM
    Users
WHERE
    mail LIKE '%@leetcode.com'
    AND SUBSTR(mail, LENGTH(mail) - LENGTH('@leetcode.com') + 1) = '@leetcode.com'
    AND
    (
        (SUBSTR(mail, 1, 1) BETWEEN 'A' AND 'Z' OR SUBSTR(mail, 1, 1) BETWEEN 'a' AND 'z')
    )
    AND
    INSTR(mail, '@') > 1
    AND mail NOT LIKE '%#%@%';


-- -- MySQL Solution
-- SELECT
--     user_id,
--     name,
--     mail
-- FROM
--     Users
-- WHERE
--     mail LIKE '%@leetcode.com'
--     AND mail REGEXP '^[a-zA-Z][a-zA-Z0-9._-]*@leetcode\\.com$';