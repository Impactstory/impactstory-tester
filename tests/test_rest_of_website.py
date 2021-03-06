import os, requests

from selenium_test_case import SeleniumTestCase, slow, online, wd, host
import tests
from tests.pages import faq_page, about_page
from nose.tools import assert_equals, raises




class TestFAQ(SeleniumTestCase):
    
    def setUp(self):
        self.page = faq_page.FaqPage(self.wd, self.host)

    def test_title(self):
        self.page.get()
        assert_equals(self.page.title, "FAQ")

    def test_which_products(self):
        self.page.get()
        assert "The number of readers who have added the article to their libraries" in self.page.html

    def test_tos_anchor_link(self):
        self.wd.get(self.page.url + "#tos")
        self.page.wait_till_loaded()
        assert_equals(self.page.title, "FAQ")

    @slow
    @online
    def test_all_links(self):
        self.page.get()
        print self.page.links
        #expected = [u'http://localhost:5000/faq#tos', u'http://www.wikipedia.org/', u'http://feedback.impactstory.org/', u'http://citedin.org/', u'http://www.crossref.org/', u'http://sciencecard.org/', u'http://www.delicious.com/', u'http://article-level-metrics.plos.org/', u'http://youtube.com/', u'http://github.com/', u'http://altmetric.com/', u'http://www.mendeley.com/groups/586171/altmetrics/papers/', u'http://blog.impactstory.org/2012/03/01/18535014681/', u'http://vimeo.com/', u'http://www.citeulike.org/', u'http://www.mendeley.com/', u'http://blog.impactstory.org/', u'http://www.topsy.com/', u'http://www.slideshare.net/', u'http://sloan.org/', u'http://altmetrics.org/manifesto/', u'http://gradschool.unc.edu/programs/royster', u'http://www.scienceseeker.org/', u'http://creativecommons.org/licenses/by/2.0/', u'http://beyond-impact.org/', u'http://figshare.com/', u'http://twitter.com/#!/ImpactStory', u'http://readermeter.org/', u'http://www.altmetric.com/', u'http://localhost:5000/#cool', u'http://localhost:5000/#limitations', u'http://localhost:5000/faq', u'https://www.zotero.org/groups/impact_factor_problems/items', u'http://pubmed.gov/', u'http://localhost:5000/about', u'https://github.com/mhahnel/Total-Impact/contributors', u'http://www.soros.org/', u'http://arxiv.org/', u'http://nsf.gov/', u'https://github.com/total-impact', u'http://www.info.sciverse.com/scopus/about', u'http://localhost:5000/#meaning', u'http://www.plumanalytics.com/', u'http://twitter.com/#!/ImpactStory_now', u'http://eprints.rclis.org/8605/', u'http://localhost:5000/settings/profile', u'http://asis.org/Bulletin/Apr-13/AprMay13_Piwowar_Priem.html', u'http://dataone.org/', u'http://localhost:5000/signup/name', u'http://impactstory.org/', u'http://localhost:5000/', u'http://wordpress.com/', u'http://www.datadryad.org/', u'http://twitter.com/', u'http://www.plos.org/']
        #assert_equals(self.page.links, expected)

        for url in self.page.links:
            print url
            r = requests.get(url, verify=False)  # don't check SSL certificates
            assert_equals(r.status_code, 200)




class TestAbout(SeleniumTestCase):
    
    def setUp(self):
        SeleniumTestCase.setUp(self) 
        self.page = about_page.AboutPage(self.wd, self.host)

    def test_title(self):
        self.page.get()
        assert_equals(self.page.title, "About")

    def test_team_anchor_link(self):
        self.wd.get(self.page.url + "#team")
        assert_equals(self.page.title, "About")

    @slow
    @online
    def test_all_links(self):
        self.page.get()
        print self.page.links
        #expected = [u'http://www.zotero.org/', u'http://localhost:5000/faq#tos', u'http://feedback.impactstory.org/', u'http://beyond-impact.org/', u'http://twitter.com/#!/ImpactStory', u'http://blog.impactstory.org/2012/03/01/18535014681/', u'http://blog.impactstory.org/', u'http://jasonpriem.org/blog', u'http://blog.impactstory.org/2013/06/17/sloan/', u'http://sloan.org/', u'http://altmetrics.org/manifesto/', u'http://twitter.com/researchremix', u'http://nsf.gov/', u'http://creativecommons.org/licenses/by/2.0/', u'http://www.plosone.org/article/info:doi/10.1371/journal.pone.0000308', u'http://localhost:5000/about', u'http://blog.impactstory.org/2012/03/29/20131290500/', u'http://www.plosone.org/article/info:doi/10.1371/journal.pone.0018657', u'https://twitter.com/jasonpriem/status/25844968813', u'http://jasonpriem.org/cv/#invited', u'http://blog.impactstory.org/2012/06/08/24638498595/', u'http://localhost:5000/faq', u'http://www.soros.org/', u'http://en.wikipedia.org/wiki/Radical_transparency', u'http://researchremix.wordpress.com/2010/10/12/journalpolicyproposal', u'http://localhost:5000/settings/profile', u'https://github.com/total-impact', u'http://localhost:5000/altmetrics.org/altmetrics12', u'http://twitter.com/#!/ImpactStory_now', u'http://researchremix.wordpress.com/', u'http://jasonpriem.org/cv/#refereed', u'http://asis.org/Bulletin/Apr-13/AprMay13_Piwowar_Priem.html', u'http://feedvis.com/', u'http://localhost:5000/signup/name', u'http://www.slideshare.net/hpiwowar', u'http://localhost:5000/', u'https://twitter.com/#!/jasonpriem', u'https://peerj.com/preprints/1/']
        #assert_equals(self.page.links, expected)

        for url in self.page.links:
            print url
            r = requests.get(url, verify=False)  # don't check SSL certificates
            assert_equals(r.status_code, 200)




class TestFeedback(SeleniumTestCase):
    
    def setUp(self):
        SeleniumTestCase.setUp(self) 
        self.url = "http://feedback.impactstory.org"

    def test_title(self):
        self.wd.get(self.url)
        title = self.wd.find_element_by_tag_name("h1").text
        expected = "General"
        assert_equals(title, expected)     
      
