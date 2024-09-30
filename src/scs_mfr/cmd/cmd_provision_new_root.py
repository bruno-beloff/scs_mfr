"""
Created on 14 Jul 2023

@author: Bruno Beloff (bruno.beloff@southcoastscience.com)
"""

import optparse

from scs_mfr import version


# --------------------------------------------------------------------------------------------------------------------

class CmdProvisionNewRoot(object):
    """unix command line handler"""

    def __init__(self):
        """
        Constructor
        """
        self.__parser = optparse.OptionParser(usage="%prog [-s] [-l LOG_LEVEL] [-x] [-v]", version=version())

        # operations...
        self.__parser.add_option("--prep-sd", "-s", action="store_true", dest="prep_sd", default=False,
                                 help="format the SD card")

        self.__parser.add_option("--log-level", "-l", type="string", action="store", dest="log_level",
                                 default='WARN', help="greengrass log level (default WARN)")

        # output...
        self.__parser.add_option("--exclude-tests", "-x", action="store_true", dest="exclude_test", default=False,
                                 help="do not perform OS checks")

        self.__parser.add_option("--verbose", "-v", action="store_true", dest="verbose", default=False,
                                 help="report narrative to stderr")

        self.__opts, self.__args = self.__parser.parse_args()


    # ----------------------------------------------------------------------------------------------------------------

    def is_valid(self):
        if self.__args:
            return False

        return True


    # ----------------------------------------------------------------------------------------------------------------

    @property
    def prep_sd(self):
        return self.__opts.prep_sd


    @property
    def log_level(self):
        return self.__opts.log_level


    @property
    def exclude_test(self):
        return self.__opts.exclude_test


    @property
    def verbose(self):
        return self.__opts.verbose


    # ----------------------------------------------------------------------------------------------------------------

    def print_help(self, file):
        self.__parser.print_help(file)


    def __str__(self, *args, **kwargs):
        return "CmdProvisionNewRoot:{prep_sd:%s, log_level:%s, exclude_test:%s, verbose:%s}" % \
                (self.prep_sd, self.log_level, self.exclude_test, self.verbose)
