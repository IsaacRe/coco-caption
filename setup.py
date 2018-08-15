from distutils.core import setup

setup(name='pycocotools',
      packages=['pycocotools'],
      package_dir = {'pycocotools': 'pycocotools'},
      version='1.0'
      )

setup(name='pycocoevalcap',
      packages=['pycocoevalcap', 'pycocoevalcap.tokenizer', 'pycocoevalcap.bleu',
                'pycocoevalcap.cider', 'pycocoevalcap.meteor', 'pycocoevalcap.spice',
                'pycocoevalcap.rouge'],
      package_data={'pycocoevalcap.meteor': ['meteor-1.5.jar', 'data/paraphrase-en.gz'],
                    'pycocoevalcap.spice': ['spice-1.0.jar', 'lib/*'],
                    'pycocoevalcap.tokenizer': ['stanford-corenlp-3.4.1.jar']},
      version='1.0'
      )
