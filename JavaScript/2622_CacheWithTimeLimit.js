var TimeLimitedCache = function() {
    this.cache = new Map();
};

/** 
 * @param {number} key
 * @param {number} value
 * @param {number} duration time until expiration in ms
 * @return {boolean} if un-expired key already existed
 */
TimeLimitedCache.prototype.set = function(key, value, duration) {
    const currentTime = Date.now();
    const existingEntry = this.cache.get(key);
    let isUnexpired = false;
    
    if (existingEntry && existingEntry.expirationTime > currentTime) {
        isUnexpired = true;
    }

    this.cache.set(key, {
        value: value,
        expirationTime: currentTime + duration
    });

    return isUnexpired;
};

/** 
 * @param {number} key
 * @return {number} value associated with key
 */
TimeLimitedCache.prototype.get = function(key) {
    const currentTime = Date.now();

    const entry = this.cache.get(key);
    if (entry && entry.expirationTime > currentTime) {
        return entry.value;
    }

    return -1;
};

/** 
 * @return {number} count of non-expired keys
 */
TimeLimitedCache.prototype.count = function() {
    const currentTime = Date.now();
    let validKeyCount = 0;
    for (const [key, entry] of this.cache) {
        if (entry.expirationTime > currentTime) {
            validKeyCount++;
        }
    } 

    return validKeyCount;
};

/**
 * const timeLimitedCache = new TimeLimitedCache()
 * timeLimitedCache.set(1, 42, 1000); // false
 * timeLimitedCache.get(1) // 42
 * timeLimitedCache.count() // 1
 */
