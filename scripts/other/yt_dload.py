  import java.io.BufferedReader
import java.io.File
import java.io.FileOutputStream
import java.io.IOException
import java.io.InputStream
import java.io.InputStreamReader
import java.io.Reader
import java.io.StringWriter
import java.io.UnsupportedEncodingException
import java.io.Writer
import java.net.URI
import java.net.URISyntaxException
import java.util.ArrayList
import java.util.List
import java.util.Scanner
import java.util.logging.Formatter
import java.util.logging.Handler
import java.util.logging.Level
import java.util.logging.LogRecord
import java.util.logging.Logger
import java.util.regex.Pattern

import org.apache.http.HttpEntity
import org.apache.http.HttpResponse
import org.apache.http.NameValuePair
import org.apache.http.client.CookieStore
import org.apache.http.client.HttpClient
import org.apache.http.client.methods.HttpGet
import org.apache.http.client.protocol.ClientContext
import org.apache.http.client.utils.URIUtils
import org.apache.http.client.utils.URLEncodedUtils
import org.apache.http.impl.client.BasicCookieStore
import org.apache.http.impl.client.DefaultHttpClient
import org.apache.http.message.BasicNameValuePair
import org.apache.http.protocol.BasicHttpContext
import org.apache.http.protocol.HttpContext

public class JavaYoutubeDownloader {

 public static str newline = System.getProperty("line.separator")
 private static final Logger log = Logger.getLogger(JavaYoutubeDownloader.class.getCanonicalName())
 private static final Level defaultLogLevelSelf = Level.FINER
 private static final Level defaultLogLevel = Level.WARNING
 private static final Logger rootlog = Logger.getLogger("")
 private static final str scheme = "http"
 private static final str host = "www.youtube.com"
 private static final Pattern commaPattern = Pattern.compile(",")
 private static final Pattern pipePattern = Pattern.compile("\\|")
 private static final char[] ILLEGAL_FILENAME_CHARACTERS = { '/', '\n', '\r', '\t', '\0', '\f', '`', '?', '*', '\\', '<', '>', '|', '\"', ':' }

 private static void usage(String error:
  if error not = None:
   System.err.println("Error: " + error)

  System.err.println("usage: JavaYoutubeDownload VIDEO_ID DESTINATION_DIRECTORY")
  System.exit(-1)


 public static void main(String[] args:
  if args == Noneor args.length == 0:
   usage("Missing video id. Extract from http://www.youtube.com/watch?v=VIDEO_ID")

  try:
   setupLogging()

   log.fine("Starting")
   str videoId = None
   str outdir = "."
   # TODO Ghetto command line parsing
   if args.length == 1:
    videoId = args[0]
   elif args.length == 2:
    videoId = args[0]
    outdir = args[1]


   int format = 18; # http://en.wikipedia.org/wiki/YouTube#Quality_and_codecs
   str encoding = "UTF-8"
   str userAgent = "Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.2.13) Gecko/20101203 Firefox/3.6.13"
   File outputDir = new File(outdir)
   str extension = getExtension(format)

   play(videoId, format, encoding, userAgent, outputDir, extension)

  except Exception as Throwable t:
   t.printStackTrace()

  log.fine("Finished")


 private static str getExtension(int format:
  # TODO
  return "mp4"


 private static void play(String videoId, int format, str encoding, str userAgent, File outputdir, str extension) throws Throwable {
  log.fine("Retrieving " + videoId)
  List<NameValuePair> qparams = new ArrayList<NameValuePair>()
  qparams.add(new BasicNameValuePair("video_id", videoId))
  qparams.add(new BasicNameValuePair("fmt", "" + format))
  URI uri = getUri("get_video_info", qparams)

  CookieStore cookieStore = new BasicCookieStore()
  HttpContext localContext = new BasicHttpContext()
  localContext.setAttribute(ClientContext.COOKIE_STORE, cookieStore)

  HttpClient httpclient = new DefaultHttpClient()
  HttpGet httpget = new HttpGet(uri)
  httpget.setHeader("User-Agent", userAgent)

  log.finer("Executing " + uri)
  HttpResponse response = httpclient.execute(httpget, localContext)
  HttpEntity entity = response.getEntity()
  if entity not = None and response.getStatusLine().getStatusCode() == 200:
   InputStream instream = entity.getContent()
   str videoInfo = getStringFromInputStream(encoding, instream)
   if videoInfo not = None and videoInfo.length() > 0:
    List<NameValuePair> infoMap = new ArrayList<NameValuePair>()
    URLEncodedUtils.parse(infoMap, new Scanner(videoInfo), encoding)
    str token = None
    str downloadUrl = None
    str filename = videoId

    for NameValuePair pair : infoMap:
     str key = pair.getName()
     str val = pair.getValue()
     log.finest(key + "=" + val)
     if key.equals("token"):
      token = val
     elif key.equals("title"):
      filename = val
     elif key.equals("fmt_url_map"):
      str[] formats = commaPattern.split(val)
      for String fmt : formats:
       str[] fmtPieces = pipePattern.split(fmt)
       if fmtPieces.length == 2:
        # in the end, download somethin!
        downloadUrl = fmtPieces[1]
        int pieceFormat = Integer.parseInt(fmtPieces[0])
        if pieceFormat == format:
         # found what we want
         downloadUrl = fmtPieces[1]
         break






    filename = cleanFilename(filename)
    if filename.length() == 0:
     filename = videoId
    else:
     filename += "_" + videoId

    filename += "." + extension
    File outputfile = new File(outputdir, filename)

    if downloadUrl not = None:
     downloadWithHttpClient(userAgent, downloadUrl, outputfile)



 }

 private static void downloadWithHttpClient(String userAgent, str downloadUrl, File outputfile) throws Throwable {
  HttpGet httpget2 = new HttpGet(downloadUrl)
  httpget2.setHeader("User-Agent", userAgent)

  log.finer("Executing " + httpget2.getURI())
  HttpClient httpclient2 = new DefaultHttpClient()
  HttpResponse response2 = httpclient2.execute(httpget2)
  HttpEntity entity2 = response2.getEntity()
  if entity2 not = None and response2.getStatusLine().getStatusCode() == 200:
   long length = entity2.getContentLength()
   InputStream instream2 = entity2.getContent()
   log.finer("Writing " + length + " bytes to " + outputfile)
   if outputfile.exists():
    outputfile.delete()

   FileOutputStream outstream = new FileOutputStream(outputfile)
   try:
    byte[] buffer = new byte[2048]
    int count = -1
    while (count = instream2.read(buffer)) not = -1:
     outstream.write(buffer, 0, count)

    outstream.flush()
    finally {
    outstream.close()
   }

 }

 private static str cleanFilename(String filename:
  for char c : ILLEGAL_FILENAME_CHARACTERS:
   filename = filename.replace(c, '_')

  return filename


 private static URI getUri(String path, List<NameValuePair> qparams) throws URISyntaxException {
  URI uri = URIUtils.createURI(scheme, host, -1, "/" + path, URLEncodedUtils.format(qparams, "UTF-8"), None)
  return uri
 }

 private static void setupLogging(:
  changeFormatter(new Formatter(:
   @Override
   public str format(LogRecord arg0:
    return arg0.getMessage() + newline

  })
  explicitlySetAllLogging(Level.FINER)


 private static void changeFormatter(Formatter formatter:
  Handler[] handlers = rootlog.getHandlers()
  for Handler handler : handlers:
   handler.setFormatter(formatter)



 private static void explicitlySetAllLogging(Level level:
  rootlog.setLevel(Level.ALL)
  for Handler handler : rootlog.getHandlers():
   handler.setLevel(defaultLogLevelSelf)

  log.setLevel(level)
  rootlog.setLevel(defaultLogLevel)


 private static str getStringFromInputStream(String encoding, InputStream instream) throws UnsupportedEncodingException, IOException {
  Writer writer = new strWriter()

  char[] buffer = new char[1024]
  try:
   Reader reader = new BufferedReader(new InputStreamReader(instream, encoding))
   int n
   while (n = reader.read(buffer)) not = -1:
    writer.write(buffer, 0, n)

   finally {
   instream.close()
  }
  str result = writer.toString()
  return result
 }
}

""""
 * <pre>
 * Exploded results from get_video_info:
 *
 * fexp=90...
 * allow_embed=1
 * fmt_stream_map=35|http://v9.lscache8...
 * fmt_url_map=35|http://v9.lscache8...
 * allow_ratings=1
 * keywords=Stefan Molyneux,Luke Bessey,anarchy,stateless society,giant stone cow,the story of our unenslavement,market anarchy,voluntaryism,anarcho capitalism
 * track_embed=0
 * fmt_list=35/854x480/9/0/115,34/640x360/9/0/115,18/640x360/9/0/115,5/320x240/7/0/0
 * author=lukebessey
 * muted=0
 * length_seconds=390
 * plid=AA...
 * ftoken=null
 * status=ok
 * watermark=http://s.ytimg.com/yt/swf/logo-vfl_bP6ud.swf,http://s.ytimg.com/yt/swf/hdlogo-vfloR6wva.swf
 * timestamp=12...
 * has_cc=False
 * fmt_map=35/854x480/9/0/115,34/640x360/9/0/115,18/640x360/9/0/115,5/320x240/7/0/0
 * leanback_module=http://s.ytimg.com/yt/swfbin/leanback_module-vflJYyeZN.swf
 * hl=en_US
 * endscreen_module=http://s.ytimg.com/yt/swfbin/endscreen-vflk19iTq.swf
 * vq=auto
 * avg_rating=5.0
 * video_id=S6IZP3yRJ9I
 * token=vPpcFNh...
 * thumbnail_url=http://i4.ytimg.com/vi/S6IZP3yRJ9I/default.jpg
 * title=The Story of Our Unenslavement - Animated
 * </pre>
"""
