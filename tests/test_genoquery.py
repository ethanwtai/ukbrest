import unittest
from os.path import isfile

from common.genoquery import GenoQuery
from tests.utils import get_repository_path
from utils.external import qctool


class UKBQueryTest(unittest.TestCase):
    def test_query_incl_range_lower_and_upper_limits_at_beginning(self):
        # prepare
        genoq = GenoQuery(get_repository_path('example01'))

        # run
        bgen_file = genoq.get_incl_range(chr=1, start=100, stop=276)

        # validate
        assert bgen_file is not None
        assert isfile(bgen_file)

        results = qctool(bgen_file)

        assert results is not None
        assert hasattr(results, 'shape')
        assert hasattr(results, 'columns')
        assert results.shape[1] == 6 + 300 * 3
        assert results.shape[0] == 3

        rsid_values = results['rsid'].unique()
        assert len(rsid_values) == 3
        assert 'rs1' in rsid_values
        assert 'rs2' in rsid_values
        assert 'rs3' in rsid_values

        assert results.loc[0, 'allele1'] == 'G'
        assert results.loc[0, 'allele2'] == 'A'

        assert results.loc[1, 'allele1'] == 'G'
        assert results.loc[1, 'allele2'] == 'C'

        assert results.loc[2, 'allele1'] == 'C'
        assert results.loc[2, 'allele2'] == 'A'

        assert results.loc[0, '1.aa'] == 0.7491
        assert results.loc[0, '1.ab'] == 0.0133
        assert results.loc[0, '1.bb'] == 0.2376

        assert results.loc[1, '2.aa'] == 0.8654
        assert results.loc[1, '2.ab'] == 0.1041
        assert results.loc[1, '2.bb'] == 0.0305 # FIXME: I understand that this should be rounded to 0.0306

        assert results.loc[2, '300.aa'] == 0.0828
        assert results.loc[2, '300.ab'] == 0.7751 # FIXME: I understand that this should be rounded to 0.7752
        assert results.loc[2, '300.bb'] == 0.1421

        pos_values = results['pos'].unique()
        assert len(pos_values) == 3
        assert results.loc[0, 'pos'] == 100
        assert results.loc[1, 'pos'] == 181
        assert results.loc[2, 'pos'] == 276

    def test_query_incl_range_lower_and_upper_limits_at_end(self):
        # prepare
        genoq = GenoQuery(get_repository_path('example01'))

        # run
        bgen_file = genoq.get_incl_range(chr=1, start=18058, stop=18389)

        # validate
        assert bgen_file is not None
        assert isfile(bgen_file)

        results = qctool(bgen_file)

        assert results is not None
        assert hasattr(results, 'shape')
        assert hasattr(results, 'columns')
        assert results.shape[1] == 6 + 300 * 3
        assert results.shape[0] == 5

        rsid_values = results['rsid'].unique()
        assert len(rsid_values) == 5
        assert 'rs246' in rsid_values
        assert 'rs247' in rsid_values
        assert 'rs248' in rsid_values
        assert 'rs249' in rsid_values
        assert 'rs250' in rsid_values

        assert results.loc[0, 'allele1'] == 'C'
        assert results.loc[0, 'allele2'] == 'A'

        assert results.loc[1, 'allele1'] == 'T'
        assert results.loc[1, 'allele2'] == 'C'

        assert results.loc[2, 'allele1'] == 'G'
        assert results.loc[2, 'allele2'] == 'C'

        assert results.loc[3, 'allele1'] == 'G'
        assert results.loc[3, 'allele2'] == 'A'

        assert results.loc[4, 'allele1'] == 'T'
        assert results.loc[4, 'allele2'] == 'C'

        assert results.loc[0, '1.aa'] == 0.0537
        assert results.loc[0, '1.ab'] == 0.9160
        assert results.loc[0, '1.bb'] == 0.0302

        assert results.loc[1, '2.aa'] == 0.0698
        assert results.loc[1, '2.ab'] == 0.9117
        assert results.loc[1, '2.bb'] == 0.0186

        assert results.loc[2, '300.aa'] == 0.0826
        assert results.loc[2, '300.ab'] == 0.0316
        assert results.loc[2, '300.bb'] == 0.8858

        assert results.loc[3, '299.aa'] == 0.7988
        assert results.loc[3, '299.ab'] == 0.1666
        assert results.loc[3, '299.bb'] == 0.0345

        assert results.loc[4, '150.aa'] == 0.0773
        assert results.loc[4, '150.ab'] == 0.8683
        assert results.loc[4, '150.bb'] == 0.0544

        pos_values = results['pos'].unique()
        assert len(pos_values) == 5
        assert results.loc[0, 'pos'] == 18058
        assert results.loc[1, 'pos'] == 18139
        assert results.loc[2, 'pos'] == 18211
        assert results.loc[3, 'pos'] == 18294
        assert results.loc[4, 'pos'] == 18389

    def test_query_incl_range_lower_limit_only(self):
        # prepare
        genoq = GenoQuery(get_repository_path('example01'))

        # run
        bgen_file = genoq.get_incl_range(chr=1, start=18058)

        # validate
        assert bgen_file is not None
        assert isfile(bgen_file)

        results = qctool(bgen_file)

        assert results is not None
        assert hasattr(results, 'shape')
        assert hasattr(results, 'columns')
        assert results.shape[1] == 6 + 300 * 3
        assert results.shape[0] == 5

        rsid_values = results['rsid'].unique()
        assert len(rsid_values) == 5
        assert 'rs246' in rsid_values
        assert 'rs247' in rsid_values
        assert 'rs248' in rsid_values
        assert 'rs249' in rsid_values
        assert 'rs250' in rsid_values

        assert results.loc[0, 'allele1'] == 'C'
        assert results.loc[0, 'allele2'] == 'A'

        assert results.loc[1, 'allele1'] == 'T'
        assert results.loc[1, 'allele2'] == 'C'

        assert results.loc[2, 'allele1'] == 'G'
        assert results.loc[2, 'allele2'] == 'C'

        assert results.loc[3, 'allele1'] == 'G'
        assert results.loc[3, 'allele2'] == 'A'

        assert results.loc[4, 'allele1'] == 'T'
        assert results.loc[4, 'allele2'] == 'C'

        assert results.loc[0, '1.aa'] == 0.0537
        assert results.loc[0, '1.ab'] == 0.9160
        assert results.loc[0, '1.bb'] == 0.0302

        assert results.loc[1, '2.aa'] == 0.0698
        assert results.loc[1, '2.ab'] == 0.9117
        assert results.loc[1, '2.bb'] == 0.0186

        assert results.loc[2, '300.aa'] == 0.0826
        assert results.loc[2, '300.ab'] == 0.0316
        assert results.loc[2, '300.bb'] == 0.8858

        assert results.loc[3, '299.aa'] == 0.7988
        assert results.loc[3, '299.ab'] == 0.1666
        assert results.loc[3, '299.bb'] == 0.0345

        assert results.loc[4, '150.aa'] == 0.0773
        assert results.loc[4, '150.ab'] == 0.8683
        assert results.loc[4, '150.bb'] == 0.0544

        pos_values = results['pos'].unique()
        assert len(pos_values) == 5
        assert results.loc[0, 'pos'] == 18058
        assert results.loc[1, 'pos'] == 18139
        assert results.loc[2, 'pos'] == 18211
        assert results.loc[3, 'pos'] == 18294
        assert results.loc[4, 'pos'] == 18389

    def test_query_incl_range_upper_limit_only(self):
        # prepare
        genoq = GenoQuery(get_repository_path('example01'))

        # run
        bgen_file = genoq.get_incl_range(chr=1, stop=276)

        # validate
        assert bgen_file is not None
        assert isfile(bgen_file)

        results = qctool(bgen_file)

        assert results is not None
        assert hasattr(results, 'shape')
        assert hasattr(results, 'columns')
        assert results.shape[1] == 6 + 300 * 3
        assert results.shape[0] == 3

        rsid_values = results['rsid'].unique()
        assert len(rsid_values) == 3
        assert 'rs1' in rsid_values
        assert 'rs2' in rsid_values
        assert 'rs3' in rsid_values

        assert results.loc[0, 'allele1'] == 'G'
        assert results.loc[0, 'allele2'] == 'A'

        assert results.loc[1, 'allele1'] == 'G'
        assert results.loc[1, 'allele2'] == 'C'

        assert results.loc[2, 'allele1'] == 'C'
        assert results.loc[2, 'allele2'] == 'A'

        assert results.loc[0, '1.aa'] == 0.7491
        assert results.loc[0, '1.ab'] == 0.0133
        assert results.loc[0, '1.bb'] == 0.2376

        assert results.loc[1, '2.aa'] == 0.8654
        assert results.loc[1, '2.ab'] == 0.1041
        assert results.loc[1, '2.bb'] == 0.0305 # FIXME: I understand that this should be rounded to 0.0306

        assert results.loc[2, '300.aa'] == 0.0828
        assert results.loc[2, '300.ab'] == 0.7751 # FIXME: I understand that this should be rounded to 0.7752
        assert results.loc[2, '300.bb'] == 0.1421

        pos_values = results['pos'].unique()
        assert len(pos_values) == 3
        assert results.loc[0, 'pos'] == 100
        assert results.loc[1, 'pos'] == 181
        assert results.loc[2, 'pos'] == 276

    def test_query_incl_range_using_file(self):
        # prepare
        genoq = GenoQuery(get_repository_path('example01'))
        # positions are not ordered in the file, but they should be returned ordered
        positions_file = get_repository_path('example01/positions01.txt')

        # run
        bgen_file = genoq.get_incl_range_from_file(2, positions_file)

        # validate
        assert bgen_file is not None
        assert isfile(bgen_file)

        results = qctool(bgen_file)

        assert results is not None
        assert hasattr(results, 'shape')
        assert hasattr(results, 'columns')
        assert results.shape[1] == 6 + 300 * 3
        assert results.shape[0] == 5

        rsid_values = results['rsid'].unique()
        assert len(rsid_values) == 5
        assert results.loc[0, 'rsid'] == 'rs2000003'
        assert results.loc[1, 'rsid'] == 'rs2000008'
        assert results.loc[2, 'rsid'] == 'rs2000094'
        assert results.loc[3, 'rsid'] == 'rs2000118'
        assert results.loc[4, 'rsid'] == 'rs2000149'

        assert results.loc[0, 'allele1'] == 'C'
        assert results.loc[0, 'allele2'] == 'G'

        assert results.loc[1, 'allele1'] == 'T'
        assert results.loc[1, 'allele2'] == 'A'

        assert results.loc[2, 'allele1'] == 'C'
        assert results.loc[2, 'allele2'] == 'G'

        assert results.loc[3, 'allele1'] == 'T'
        assert results.loc[3, 'allele2'] == 'C'

        assert results.loc[4, 'allele1'] == 'G'
        assert results.loc[4, 'allele2'] == 'T'

        assert results.loc[0, '1.aa'] == 0.7888
        assert results.loc[0, '1.ab'] == 0.1538
        assert results.loc[0, '1.bb'] == 0.0573

        assert results.loc[1, '2.aa'] == 0.8776
        assert results.loc[1, '2.ab'] == 0.0670
        assert results.loc[1, '2.bb'] == 0.0554

        assert results.loc[2, '3.aa'] == 0.0553
        assert results.loc[2, '3.ab'] == 0.0939
        assert results.loc[2, '3.bb'] == 0.8509

        assert results.loc[3, '1.aa'] == 0.1219
        assert results.loc[3, '1.ab'] == 0.8459
        assert results.loc[3, '1.bb'] == 0.0323

        assert results.loc[4, '2.aa'] == 0.0137
        assert results.loc[4, '2.ab'] == 0.0953
        assert results.loc[4, '2.bb'] == 0.8909

        pos_values = results['pos'].unique()
        assert len(pos_values) == 5
        assert results.loc[0, 'pos'] == 300
        assert results.loc[1, 'pos'] == 661
        assert results.loc[2, 'pos'] == 7181
        assert results.loc[3, 'pos'] == 8949
        assert results.loc[4, 'pos'] == 11226

# position in file that does not exist?