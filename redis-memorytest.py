__author__ = 'huangpengcheng'
import redis
import uuid
import time
import logging

# Connect to redis
r = redis.Redis(host='197.3.84.120', port=6679, db=0)
LOGFILE = 'redis.log'

logging.basicConfig(filename=LOGFILE,level=logging.DEBUG,filemode='a')

def testsets():
    # number of sets
    for num_sets in (100,1000, 10000):
        for set_size in (100, 1000, 10000):
            r.flushall()
            time.sleep(1.0)
            initial_size = r.dbsize()
            initial_info = r.info()

            logging.debug("For %s sets with %s values." % (num_sets, set_size))
            for i in xrange(0, num_sets):
                # number of items per set
                for j in xrange(0, set_size):
                    r.sadd("set.%s" % (str(i).zfill(len(str(num_sets))),), str(uuid.uuid4()))

            final_size = r.dbsize()
            final_info = r.info()

            logging.debug("Keys: %s => %s" % (initial_size, final_size))
            logging.debug("Memory: %s => %s" % (initial_info['used_memory_human'],
                                        final_info['used_memory_human']))
            logging.debug("The single size of key is %s, value is %s" % (
                str(len('set.')+len(str(num_sets))),
                len(str(uuid.uuid4()))
            ))
            r.flushall()

def testzsets():
    # number of sets
    for num_sets in (100,1000,10000):
        for set_size in (100,1000,10000):
            r.flushall()
            time.sleep(1.0)
            initial_size = r.dbsize()
            initial_info = r.info()

            logging.debug("For %s zsets with %s values." % (num_sets, set_size))
            for i in xrange(0, num_sets):
                # number of items per set
                for j in xrange(0, set_size):
                            time.sleep(0.001)
                            r.zadd("zset.%s" % (str(i).zfill(len(str(num_sets))),), str(uuid.uuid4()), time.time())

            final_size = r.dbsize()
            final_info = r.info()

            logging.debug("Keys: %s => %s" % (initial_size, final_size))
            logging.debug("Memory: %s => %s" % (initial_info['used_memory_human'],
                                        final_info['used_memory_human']))
            logging.debug("The single size of key is %s, value is %s" % (
                str(len('zset.')+len(str(num_sets))),
                len(str(uuid.uuid4())+str(time.time()))
            ))
            r.flushall()

def testhash():
    for num_hashes in (100,1000,10000,):
        for hash_size in (100,1000,10000):
            r.flushall()
            time.sleep(1.0)
            initial_size = r.dbsize()
            initial_info = r.info()

            logging.debug("For %s hash with %s values." % (num_hashes, hash_size))
            for i in xrange(0, num_hashes):
                for j in xrange(0, hash_size):
                    r.hset("hash.%s" % str(i).zfill(len(str(num_hashes))), str(uuid.uuid4()), time.time())

	    final_size = r.dbsize()
	    final_info = r.info()

            logging.debug("Keys: %s => %s" % (initial_size, final_size))
            logging.debug("Memory: %s => %s" % (initial_info['used_memory_human'],
                                        final_info['used_memory_human']))
            logging.debug("The single size of key is %s, value is %s" % (
                str(len('hash.')+len(str(num_hashes))),
                len(str(uuid.uuid4())+str(time.time()))
            ))
            r.flushall()

def testlist():
    for num_list in (100, 1000,10000):
        for list_size in (100, 1000,10000):
            r.flushall()
            time.sleep(1.0)
            initial_size = r.dbsize()
            initial_info = r.info()

            logging.debug("For %s list with %s values." % (num_list, list_size))
            for i in xrange(0, num_list):
                for j in xrange(0, list_size):
                    r.lpush("list.%s" % str(i).zfill(len(str(num_list))), str(uuid.uuid4()))

	    final_size = r.dbsize()
	    final_info = r.info()

            logging.debug("Keys: %s => %s" % (initial_size, final_size))
            logging.debug("Memory: %s => %s" % (initial_info['used_memory_human'],
                                        final_info['used_memory_human']))
            logging.debug("The single size of key is %s, value is %s" % (
                str(len('list.')+len(str(num_list))),
                len(str(uuid.uuid4()))
            ))
            r.flushall()

def teststring():
    for num_strings in (100,1000,10000,100000,1000000,10000000):
        r.flushall()
        time.sleep(1.0)
        initial_size = r.dbsize()
        initial_info = r.info()

        logging.debug("For %s string" % (num_strings,))
        for i in xrange(0, num_strings):
            r.set(str(uuid.uuid4()), time.time())
        final_size = r.dbsize()
        final_info = r.info()

        logging.debug("Keys: %s => %s" % (initial_size, final_size))
        logging.debug("Memory: %s => %s" % (initial_info['used_memory_human'],
                                        final_info['used_memory_human']))
        logging.debug("The single size of key is %s, value is %s" % (
            str(len(str(uuid.uuid4()))),
            len(str(time.time()))
        ))
        r.flushall()

if __name__=='__main__':
    testsets()
    testzsets()
    testhash()
    testlist()
    teststring()
