module Jekyll class PlaceAds < Liquid::Tag

  def initialize(tag_name, text, tokens)
    super
    @text = text
  end

  def render(context)
    '<!-- Con un tag (plugin)-->
    <script async src="//pagead2.googlesyndication.com/pagead/js/adsbygoogle.js"></script>
    <ins class="adsbygoogle" style="display:block;background-color:transparent" data-ad-client="ca-pub-0000000000000000" data-ad-slot="0000000000" data-ad-format="auto" data-full-width-responsive="true"></ins><script>(adsbygoogle = window.adsbygoogle || []).push({});
    </script>'
  end
end
end

Liquid::Template.register_tag('anuncio', Jekyll::PlaceAds)
