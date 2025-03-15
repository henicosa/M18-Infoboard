def get_feed_entries():
    
    # This is how a feed entry should look like
    feed_item_1 = {
        # This is the type of the feed, e.g pinnwannd, instagram etc.
        "type": "dummy",
        # This is the publication date and time
        "pubDate" : "Tue, 07 Mar 2023 09:46:00 +0100",
        # This is the publication date and time in unix time (was a bit lazy in this example)
        "pubUnix" : 0,
        # This is the title of the feed element
        "title": "Johanna-Maria Vanderwalle: HIWI gesucht - Professur Angewandte Mathematik",
        # This is the link to the original resource
        "link": "https://www.uni-weimar.de/universitaet/aktuell/pinnwaende/titel/hiwi-gesucht-professur-angewandte-mathematik/",
        # This is a short summary of the content
        "summary": "Zum n&amp;auml;chstm&amp;ouml;glichen Zeitpunkt suchen wir in der Professur Angewandte Mathematik eine/einen studentische(n) Assistent*in im Umfang von ca...",
        # This is the content
        "content" : """<p class="bodytext">Zum nächstmöglichen Zeitpunkt suchen wir in der Professur Angewandte Mathematik eine/einen studentische(n) Assistent*in im Umfang von ca. 15-20h/Monat zu einem Stundensatz von 12 EUR/h.</p><p>Zu den Aufgaben gehören unterstützende Tätigkeiten in Forschung und Lehre, z.B. in den Bereichen Datenerfassung, Recherche, Auswertung, sowie die Betreuung von wissenschaftlichen Workshops.</p><p>Bei Interesse melden Sie sich bitte bei Frau Johanna-M. Vanderwalle unter</p><p><a href="mailto:johanna-maria.vanderwalle@uni-weimar.de" rel="noopener noreferrer" target="_blank">johanna-maria.vanderwalle@uni-weimar.de</a>.</p><p>Professur Angewandte Mathematik</p><p><a href="https://www.uni-weimar.de/de/bauingenieurwesen/professuren/angewandte-mathematik/" rel="noopener noreferrer" target="_blank"><a href="https://www.uni-weimar.de/de/bauingenieurwesen/professuren/angewandte-mathematik/" target="_blank">www.uni-weimar.de/de/bauingenieurwesen/professuren/angewandte-mathematik/</a></a></p>""",
        # Encoding of the content
        "content_encoding" : "html",
        # Tags (could be parsed out of hashtags or something else)
        "tags" : ["Universität", "Biete / Suche", "Piazza"],
        # link to a web image that should be displayed
        "image" : None
    }

    feed_item_2 = {
        "type": "dummy",
        "pubDate" : "Mon, 06 Mar 2023 21:04:00 +0100",
        "pubUnix" : 1,
        "title": "Sophie Foster: BIBLIOTHEK DER KÜNSTLER*INNEN, WEIMAR - 08 MAR - WER IST DIESE FRAU? / WHO IS THIS WOMAN?",
        "link": "https://www.uni-weimar.de/universitaet/aktuell/pinnwaende/titel/bibliothek-der-kuenstlerinnen-weimar-08-mar-wer-ist-diese-frau-who-is-this-woman/",
        "summary": "08.03-29.03.23 Vernissage 7pm11m3 ProjektraumKarl-Liebknecht-Stra&amp;szlig;e 16, Weimar&amp;nbsp;Anl&amp;auml;sslich des Internationalen Frauentags und des...",
        "content" : """
<![CDATA[<p style="margin-left:0cm; margin-right:0cm" class="bodytext">08.03-29.03.23 Vernissage 7pm</p><p style="margin-left:0cm; margin-right:0cm">11m3 Projektraum</p><p style="margin-left:0cm; margin-right:0cm">Karl-Liebknecht-Straße 16, Weimar</p><p style="margin-left:0cm; margin-right:0cm">&nbsp;</p><p style="margin-left:0cm; margin-right:0cm">Anlässlich des Internationalen Frauentags und des Monats der Frauengeschichte freuen sich Sophie Foster und Maria Paula Maldonado, ihre neues Projekt <em>Wer ist diese Frau? / Who is this Woman?</em> das darauf abzielt, die weniger bekannten Frauen des Bauhauses zu erforschen und zu feiern.</p><p style="margin-left:0cm; margin-right:0cm"><br>Inspiriert durch ein Foto aus dem Bauhaus-Archiv: Eine Frau mit einer Maske von Oskar Schlemmer, die auf einem Stuhl von Marcel Breuer sitzt, trägt ein Kleid von Lis Beyer. Sofort wurde die Frage gestellt: “Wer ist diese Frau?” Es gibt viele Spekulationen darüber, wer diese Frau sein könnte, wobei die Bauhäuser*innen Lis Beyer, Ise Gropius, Ruth Hollos und Immeke Schwollmann mit ihrer Identität in Verbindung gebracht werden. Mit dieser partizipativen Ausstellung laden wir die Besucher*innen ein, mehr über diese Frauen zu erfahren und über die weiteren Auswirkungen dieser Anonymität nachzudenken.</p><p style="margin-left:0cm; margin-right:0cm"><br>Darüber hinaus ist die <em>Bibliothek der Künstler*innen Weimar</em> Teil des <em>FLINTA*-Kampftages</em> und veranstaltet vor der Vernissage von 15:30-18:30 Uhr auf dem Theaterplatz einen speziellen Tag der offenen Bibliothek, an dem sich Besucher*innen über das Projekt und die Ausstellung informieren und eigene Beiträge einbringen können. Weitere Informationen finden Sie auf den beiden Websites <a href="http://11m3.de" target="_blank">11m3.de</a> und <a href="http://bdkw.org" target="_blank">bdkw.org</a> oder auf den Instagram-Accounts <a href="https://www.instagram.com/11m3_projektraum/" target="_blank">@11m3_projektraum</a> und <a href="https://www.instagram.com/bdk_weimar/" target="_blank">@bdkw_org</a>.</p><p style="margin-left:0cm; margin-right:0cm">&nbsp;</p><p style="margin-left:0cm; margin-right:0cm"><strong>+++</strong></p><p style="margin-left:0cm; margin-right:0cm">&nbsp;</p><p style="margin-left:0cm; margin-right:0cm">To commemorate <em>International Women’s Day</em> and <em>Women’s History Month</em>, Sophie Foster and Maria Paula&nbsp;Maldonado&nbsp;are excited to share their&nbsp;upcoming window exhibition, <em>Wer ist diese Frau? / Who is this Woman?</em> which aims to explore and celebrate the lesser-known women of the Bauhaus.</p><p style="margin-left:0cm; margin-right:0cm">&nbsp;</p><p style="margin-left:0cm; margin-right:0cm">Inspired by a photo from the Bauhaus archive: a woman wearing a mask by Oskar Schlemmer, sitting on a chair by Marcel Breuer, wearing a dress by Lis Beyer. Immediately, the question was asked, “Who is this woman?” There is much speculation about who she could be, with the Bauhaus creatives Lis Beyer, Ise Gropius, Ruth Hollós and Immeke Schwollmann, linked to her identity. Through this participatory exhibition, we invite visitors to learn more about these women and consider the implications of this anonymity.</p><p style="margin-left:0cm; margin-right:0cm">&nbsp;</p><p style="margin-left:0cm; margin-right:0cm">Additionally, <em>Bibliothek der Künstler*innen Weimar</em> is part of the <em>FLINTA* Kampftag</em> programme and will host a special Open Library Day before the vernissage at Theaterplatz from 15:30-18:30 where visitors can find out more about the project and the exhibition as well as offer their own contributions. For more information you can visit both websites <a href="http://11m3.de" target="_blank">11m3.de</a> and <a href="http://bdkw.org" target="_blank">bdkw.org</a> or keep regularly updated via their Instagram accounts <a href="https://www.instagram.com/11m3_projektraum/" target="_blank">@11m3_projektraum</a> and <a href="https://www.instagram.com/bdk_weimar/" target="_blank">@bdkw_org</a>.</p><p style="margin-left:0cm; margin-right:0cm">&nbsp;</p><p style="margin-left:0cm; margin-right:0cm">&nbsp;</p><p>&nbsp;</p>]]>
""",
        "content_encoding" : "html",
        "tags" : ["Universität", "Kunst und Gestaltung", "Piazza"],
        "image" : "https://www.uni-weimar.de/fileadmin/_processed_/7/f/csm_83_55a41ab0b6.png"
    }
    entries = [feed_item_1, feed_item_2]
    return entries