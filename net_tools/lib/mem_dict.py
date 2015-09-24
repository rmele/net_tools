
class MemDict:
    def __init__(self):
        pass

    def new(self, num_buckets=256):
        """Initializes a Map with the given number of buckets."""
        aMap = []
        for i in range(0, num_buckets):
            aMap.append([])
        return aMap

    def hash_key(self, aMap, key):
        """Given a key this will create a number and then convert it to
        an index for the aMap's buckets."""
        return hash(key) % len(aMap)

    def get_bucket(self, aMap, key):
        """Given a key, find the bucket where it would go."""
        bucket_id = self.hash_key(aMap, key)
        return aMap[bucket_id]

    def get_slot(self, aMap, key, default=None):
        """
        Returns the index, key, and value of a slot found in a bucket.
        Returns -1, key, and default (None if not set) when not found.
        """
        bucket = self.get_bucket(aMap, key)

        for i, kv in enumerate(bucket):
            k, v = kv
            if key == k:
                return i, k, v

        return -1, key, default

    def get(self, aMap, key, default=None):
        """Gets the value in a bucket for the given key, or the default."""
        i, k, v = self.get_slot(aMap, key, default=default)
        return v

    def set(self, aMap, key, value):
        """Sets the key to the value, replacing any existing value."""
        bucket = self.get_bucket(aMap, key)
        i, k, v = self.get_slot(aMap, key)

        if i >= 0:
            # the key exists, replace it
            bucket[i] = (key, value)
        else:
            # the key does not, append to create it
            bucket.append((key, value))

    def delete(self, aMap, key):
        """Deletes the given key from the Map."""
        bucket = self.get_bucket(aMap, key)

        for i in xrange(len(bucket)):
            k, v = bucket[i]
            if key == k:
                del bucket[i]
                break

    def list(self, aMap):
        """Prints out what's in the Map."""
        bucket_list = []
        for bucket in aMap:
            if bucket:
                for k, v in bucket:
                    bucket_list.append((k, v))
        return bucket_list

if __name__ == "__main__":
    hashmap = MemDict()

    combo = hashmap.new()
    hashmap.set(combo, 'cb_l_a_freq_type_a', 'bypass')
    hashmap.set(combo, 'cb_l_a_freq_type_b', 'bypass')
    hashmap.set(combo, 'cb_l_a_freq_type_c', 'bypass')
    hashmap.set(combo, 'cb_l_a_freq_type_d', 'bypass')

    dsb = hashmap.new()
    hashmap.set(dsb, 'dsb_l_a_freq_a', 21.1)
    hashmap.set(dsb, 'dsb_l_a_freq_b', 22.1)
    hashmap.set(dsb, 'dsb_l_a_freq_c', 23.1)
    hashmap.set(dsb, 'dsb_l_a_freq_d', 24.1)

    hashmap.set(dsb, 'dsb_l_a_gain_a', 1.1)
    hashmap.set(dsb, 'dsb_l_a_gain_b', 1.2)
    hashmap.set(dsb, 'dsb_l_a_gain_c', 1.3)
    hashmap.set(dsb, 'dsb_l_a_gain_d', 1.4)

    hashmap.set(dsb, 'dsb_l_a_bw_a', 1.6)
    hashmap.set(dsb, 'dsb_l_a_bw_b', 2.7)
    hashmap.set(dsb, 'dsb_l_a_bw_c', 3.8)
    hashmap.set(dsb, 'dsb_l_a_bw_d', 4.9)

    freq = hashmap.new()
    hashmap.set(freq, 'l_a_freq_a', [hashmap.get(combo,'cb_l_a_freq_type_a'), hashmap.get(dsb,'dsb_l_a_freq_a'), hashmap.get(dsb,'dsb_l_a_gain_a'), hashmap.get(dsb,'dsb_l_a_bw_a')])
    hashmap.set(freq, 'l_a_freq_b', [hashmap.get(combo,'cb_l_a_freq_type_b'), hashmap.get(dsb,'dsb_l_a_freq_b'), hashmap.get(dsb,'dsb_l_a_gain_b'), hashmap.get(dsb,'dsb_l_a_bw_b')])
    hashmap.set(freq, 'l_a_freq_c', [hashmap.get(combo,'cb_l_a_freq_type_c'), hashmap.get(dsb,'dsb_l_a_freq_c'), hashmap.get(dsb,'dsb_l_a_gain_c'), hashmap.get(dsb,'dsb_l_a_bw_c')])
    hashmap.set(freq, 'l_a_freq_d', [hashmap.get(combo,'cb_l_a_freq_type_d'), hashmap.get(dsb,'dsb_l_a_freq_d'), hashmap.get(dsb,'dsb_l_a_gain_d'), hashmap.get(dsb,'dsb_l_a_bw_d')])

    look_up = 'l_a_freq_d'
    # print look_up, hashmap.get(freq, '%s' % look_up)
    print hashmap.list(combo)
