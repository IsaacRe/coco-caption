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
      version='1.0'
      )
