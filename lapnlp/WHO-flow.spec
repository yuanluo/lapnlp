# The full description of 
gsentencize: sentencize-opennlp
gsentencize-ver: 1.5.2
gsentencize-setting:
gsentence-split: \n *\n

gtokenize: tokenize-link
gtokenize-ver: 4.7.4 # need to check link parser
gtokenize-setting: customized

gnum-recognize: num-recognize
gnum-recognize-ver: 1.0
gnum-recognize-setting: 


gtagize: tagize-opennlp
gtagize-ver: 1.5.2
gtagize-setting: umls-tag

gchunkize: chunkize-opennlp
gchunkize-ver: 1.5.2
gchunkize-setting: umls-tag

gparse: parse-stanford-tagged
gparse-ver: 2012-02-03
gparse-setting: umls-tag
gallcap2normal: yes

gumlsize: umlsize
gumlsize-ver: 2011AB
gumlsize-setting: str->cui


gevent-frame: event-frame
gevent-frame-ver: 1.0
gevent-frame-setting: plain, parse-stanford-tagged
gevent-frame-type: plain_graph # or factor_graph
gevent-frame-outdir: 
gevent-frame-umls: tui-annotation
gevent-frame-max-entity-stn-depth: 3
gevent-frame-max-event-stn-depth: 4
gevent-frame-min-size: 1 # was using 3
gevent-frame-noun-node: mesh

ghierarchize: hierarchize-syn-sem
ghierarchize-ver: 1.0
ghierarchize-setting: umls-and-NP


ghier-parse: parse-stanford-hier-tagged
ghier-parse-ver: 2012-03-09
ghier-parse-setting: umls-tag, umls-and-NP-pnode


ghier-event-frame: hier-event-frame
ghier-event-frame-ver: 1.0
ghier-event-frame-setting: plain, parse-stanford-hier-tagged
ghier-event-frame-type: plain_graph # or factor_graph
ghier-event-frame-outdir:
ghier-event-frame-umls: tui-annotation
ghier-event-frame-max-entity-stn-depth: 3
ghier-event-frame-max-event-stn-depth: 4
ghier-event-frame-min-size: 1 # was using 3
