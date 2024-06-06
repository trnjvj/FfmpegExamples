
    Convert an input media file to a different format, by re-encoding media streams:

    ffmpeg -i input.avi output.mp4

    Set the video bitrate of the output file to 64 kbit/s:

    ffmpeg -i input.avi -b:v 64k -bufsize 64k output.mp4

    Force the frame rate of the output file to 24 fps:

    ffmpeg -i input.avi -r 24 output.mp4

    Force the frame rate of the input file (valid for raw formats only) to 1 fps and the frame rate of the output file to 24 fps:

    ffmpeg -r 1 -i input.m2v -r 24 output.mp4








Decoding AVOptions can be passed to loopback decoders by placing them before -dec, analogously to input/output options.

E.g. the following example:

ffmpeg -i INPUT                                        \
  -map 0:v:0 -c:v libx264 -crf 45 -f null -            \
  -threads 3 -dec 0:0                                  \
  -filter_complex '[0:v][dec:0]hstack[stack]'          \
  -map '[stack]' -c:v ffv1 OUTPUT







input file 'A.avi'
      stream 0: video 640x360
      stream 1: audio 2 channels

input file 'B.mp4'
      stream 0: video 1920x1080
      stream 1: audio 2 channels
      stream 2: subtitles (text)
      stream 3: audio 5.1 channels
      stream 4: subtitles (text)

input file 'C.mkv'
      stream 0: video 1280x720
      stream 1: audio 2 channels
      stream 2: subtitles (image)
      
      
      
      
      
      
      
      
      
      ffmpeg -i A.avi -i B.mp4 out1.mkv out2.wav -map 1:a -c:a copy out3.mov
      
      
      
      
      
      ffmpeg -i C.mkv out1.mkv -c:s dvdsub -an out2.mkv
      
      
      
      
      
      
      ffmpeg -i A.avi -i C.mkv -i B.mp4 -filter_complex "overlay" out1.mp4 out2.srt
      
      
      
      
      
      
      
      ffmpeg -i A.avi -i B.mp4 -i C.mkv -filter_complex "[1:v]hue=s=0[outv];overlay;aresample" \
       -map '[outv]' -an        out1.mp4 \
                                out2.mkv \
       -map '[outv]' -map 1:a:0 out3.mkv
       
       
       
       
       
       
       
       
       
       The above command will fail, as the output pad labelled [outv] has been mapped twice. None of the output files shall be processed.

ffmpeg -i A.avi -i B.mp4 -i C.mkv -filter_complex "[1:v]hue=s=0[outv];overlay;aresample" \
       -an        out1.mp4 \
                  out2.mkv \
       -map 1:a:0 out3.mkv

This command above will also fail as the hue filter output has a label, [outv], and hasn’t been mapped anywhere.

The command should be modified as follows,

ffmpeg -i A.avi -i B.mp4 -i C.mkv -filter_complex "[1:v]hue=s=0,split=2[outv1][outv2];overlay;aresample" \
        -map '[outv1]' -an        out1.mp4 \
                                  out2.mkv \
        -map '[outv2]' -map 1:a:0 out3.mkv










ffmpeg -i INPUT -/filter:v filter.script OUTPUT





ffmpeg -sources pulse,server=192.168.0.4



ffmpeg -sinks pulse,server=192.168.0.4





ffmpeg -loglevel repeat+level+verbose -i input output




ffmpeg [...] -loglevel +repeat



FFREPORT=file=ffreport.log:level=32 ffmpeg -i input output



ffmpeg -cpuflags -sse+mmx ...
ffmpeg -cpuflags mmx ...
ffmpeg -cpuflags 0 ...



ffmpeg -cpucount 2




ffmpeg -i input.flac -id3v2_version 3 out.mp3



ffmpeg -i multichannel.mxf -map 0:v:0 -map 0:a:0 -map 0:a:0 -c:a:0 ac3 -b:a:0 640k -ac:a:1 2 -c:a:1 aac -b:2 128k out.mp4



ffmpeg -i INPUT -map 0 -c:v libx264 -c:a copy OUTPUT



ffmpeg -i INPUT -map 0 -c copy -c:v:1 libx264 -c:a:137 libvorbis OUTPUT



ffmpeg -i in.avi -metadata title="my title" out.flv



ffmpeg -i INPUT -metadata:s:a:0 language=eng OUTPUT




For example, to make the second audio stream the default stream:

ffmpeg -i in.mkv -c copy -disposition:a:1 default out.mkv

To make the second subtitle stream the default stream and remove the default disposition from the first subtitle stream:

ffmpeg -i in.mkv -c copy -disposition:s:0 0 -disposition:s:1 default out.mkv

To add an embedded cover/thumbnail:

ffmpeg -i in.mp4 -i IMAGE -map 0 -map 1 -c copy -c:v:1 png -disposition:v:1 attached_pic out.mp4







E.g. to create an scalable 5.1 IAMF file from several WAV input files

ffmpeg -i front.wav -i back.wav -i center.wav -i lfe.wav
-map 0:0 -map 1:0 -map 2:0 -map 3:0 -c:a opus
-stream_group type=iamf_audio_element:id=1:st=0:st=1:st=2:st=3,
demixing=parameter_id=998,
recon_gain=parameter_id=101,
layer=ch_layout=stereo,
layer=ch_layout=5.1,
-stream_group type=iamf_mix_presentation:id=2:stg=0:annotations=en-us=Mix_Presentation,
submix=parameter_id=100:parameter_rate=48000|element=stg=0:parameter_id=100:annotations=en-us=Scalable_Submix|layout=sound_system=stereo|layout=sound_system=5.1
-streamid 0:0 -streamid 1:1 -streamid 2:2 -streamid 3:3 output.iamf

To copy the two stream groups (Audio Element and Mix Presentation) from an input IAMF file with four streams into an mp4 output

ffmpeg -i input.iamf -c:a copy -stream_group map=0=0:st=0:st=1:st=2:st=3 -stream_group map=0=1:stg=0
-streamid 0:0 -streamid 1:1 -streamid 2:2 -streamid 3:3 output.mp4









ffmpeg -i myfile.avi -target vcd /tmp/vcd.mpg

Nevertheless you can specify additional options as long as you know they do not conflict with the standard, as in:

ffmpeg -i myfile.avi -target vcd -bf 2 /tmp/vcd.mpg

The parameters set for each target are as follows.

VCD

pal:
-f vcd -muxrate 1411200 -muxpreload 0.44 -packetsize 2324
-s 352x288 -r 25
-codec:v mpeg1video -g 15 -b:v 1150k -maxrate:v 1150k -minrate:v 1150k -bufsize:v 327680
-ar 44100 -ac 2
-codec:a mp2 -b:a 224k

ntsc:
-f vcd -muxrate 1411200 -muxpreload 0.44 -packetsize 2324
-s 352x240 -r 30000/1001
-codec:v mpeg1video -g 18 -b:v 1150k -maxrate:v 1150k -minrate:v 1150k -bufsize:v 327680
-ar 44100 -ac 2
-codec:a mp2 -b:a 224k

film:
-f vcd -muxrate 1411200 -muxpreload 0.44 -packetsize 2324
-s 352x240 -r 24000/1001
-codec:v mpeg1video -g 18 -b:v 1150k -maxrate:v 1150k -minrate:v 1150k -bufsize:v 327680
-ar 44100 -ac 2
-codec:a mp2 -b:a 224k

SVCD

pal:
-f svcd -packetsize 2324
-s 480x576 -pix_fmt yuv420p -r 25
-codec:v mpeg2video -g 15 -b:v 2040k -maxrate:v 2516k -minrate:v 0 -bufsize:v 1835008 -scan_offset 1
-ar 44100
-codec:a mp2 -b:a 224k

ntsc:
-f svcd -packetsize 2324
-s 480x480 -pix_fmt yuv420p -r 30000/1001
-codec:v mpeg2video -g 18 -b:v 2040k -maxrate:v 2516k -minrate:v 0 -bufsize:v 1835008 -scan_offset 1
-ar 44100
-codec:a mp2 -b:a 224k

film:
-f svcd -packetsize 2324
-s 480x480 -pix_fmt yuv420p -r 24000/1001
-codec:v mpeg2video -g 18 -b:v 2040k -maxrate:v 2516k -minrate:v 0 -bufsize:v 1835008 -scan_offset 1
-ar 44100
-codec:a mp2 -b:a 224k

DVD

pal:
-f dvd -muxrate 10080k -packetsize 2048
-s 720x576 -pix_fmt yuv420p -r 25
-codec:v mpeg2video -g 15 -b:v 6000k -maxrate:v 9000k -minrate:v 0 -bufsize:v 1835008
-ar 48000
-codec:a ac3 -b:a 448k

ntsc:
-f dvd -muxrate 10080k -packetsize 2048
-s 720x480 -pix_fmt yuv420p -r 30000/1001
-codec:v mpeg2video -g 18 -b:v 6000k -maxrate:v 9000k -minrate:v 0 -bufsize:v 1835008
-ar 48000
-codec:a ac3 -b:a 448k

film:
-f dvd -muxrate 10080k -packetsize 2048
-s 720x480 -pix_fmt yuv420p -r 24000/1001
-codec:v mpeg2video -g 18 -b:v 6000k -maxrate:v 9000k -minrate:v 0 -bufsize:v 1835008
-ar 48000
-codec:a ac3 -b:a 448k

DV

pal:
-f dv
-s 720x576 -pix_fmt yuv420p -r 25
-ar 48000 -ac 2

ntsc:
-f dv
-s 720x480 -pix_fmt yuv411p -r 30000/1001
-ar 48000 -ac 2

film:
-f dv
-s 720x480 -pix_fmt yuv411p -r 24000/1001
-ar 48000 -ac 2










ffmpeg -i INPUT -attach DejaVuSans.ttf -metadata:s:2 mimetype=application/x-truetype-font out.mkv




ffmpeg -dump_attachment:t:0 out.ttf -i INPUT



ffmpeg -dump_attachment:t "" -i INPUT




ffmpeg -i foo.mov -c:v libxvid -pass 1 -an -f rawvideo -y NUL
ffmpeg -i foo.mov -c:v libxvid -pass 1 -an -f rawvideo -y /dev/null





-force_key_frames 0:05:00,chapters-0.1


-force_key_frames expr:gte(t,n_forced*5)


-force_key_frames expr:if(isnan(prev_forced_t),gte(t,13),gte(t,prev_forced_t+5))




    To map ALL streams from the first input file to output

    ffmpeg -i INPUT -map 0 output

select specific stream

    If you have two audio streams in the first input file, these streams are identified by 0:0 and 0:1. You can use -map to select which streams to place in an output file. For example:

    ffmpeg -i INPUT -map 0:1 out.wav

    will map the second input stream in INPUT to the (single) output stream in out.wav.
create multiple streams

    To select the stream with index 2 from input file a.mov (specified by the identifier 0:2), and stream with index 6 from input b.mov (specified by the identifier 1:6), and copy them to the output file out.mov:

    ffmpeg -i a.mov -i b.mov -c copy -map 0:2 -map 1:6 out.mov

create multiple streams 2

    To select all video and the third audio stream from an input file:

    ffmpeg -i INPUT -map 0:v -map 0:a:2 OUTPUT

negative map

    To map all the streams except the second audio, use negative mappings

    ffmpeg -i INPUT -map 0 -map -0:a:1 OUTPUT

optional map

    To map the video and audio streams from the first input, and using the trailing ?, ignore the audio mapping if no audio streams exist in the first input:

    ffmpeg -i INPUT -map 0:v -map 0:a? OUTPUT

map by language

    To pick the English audio stream:

    ffmpeg -i INPUT -map 0:m:language:eng OUTPUT








For example to copy metadata from the first stream of the input file to global metadata of the output file:

ffmpeg -i in.ogg -map_metadata 0:s:0 out.mp3

To do the reverse, i.e. copy global metadata to all audio streams:

ffmpeg -i in.mkv -map_metadata:s:a 0:g out.mkv






For example, to set the stream 0 PID to 33 and the stream 1 PID to 36 for an output mpegts file:

ffmpeg -i inurl -streamid 0:33 -streamid 1:36 out.ts




bitstream_filters is a comma-separated list of bitstream filter specifications, each of the form

filter[=optname0=optval0:optname1=optval1:...]





ffmpeg -bsf:v h264_mp4toannexb -i h264.mp4 -c:v copy -an out.h264




ffmpeg -i file.mov -an -vn -bsf:s mov2textsub -c:s copy -f rawvideo sub.txt



ffmpeg -i input.mpg -timecode 01:02:03.04 -r 30000/1001 -s ntsc output.mpg



ffmpeg -i input.mkv \
  -filter_complex '[0:v]scale=size=hd1080,split=outputs=2[for_enc][orig_scaled]' \
  -c:v libx264 -map '[for_enc]' output.mkv \
  -dec 0:0 \
  -filter_complex '[dec:0][orig_scaled]hstack[stacked]' \
  -map '[stacked]' -c:v ffv1 comparison.mkv
  
  
  
  
  
  
  ffmpeg -i video.mkv -i image.png -filter_complex '[0:v][1:v]overlay[out]' -map
'[out]' out.mkv



ffmpeg -i video.mkv -i image.png -filter_complex 'overlay[out]' -map
'[out]' out.mkv



ffmpeg -i video.mkv -i image.png -filter_complex 'overlay' out.mkv


ffmpeg -i input.ts -filter_complex \
  '[#0x2ef] setpts=PTS+1/TB [sub] ; [#0x2d0] [sub] overlay' \
  -sn -map '#0x2dc' output.mkv
  
  
  
  ffmpeg -filter_complex 'color=c=red' -t 5 out.mkv
  
  
  
  frame= FRAME q= FRAME_QUALITY PSNR= PSNR f_size= FRAME_SIZE s_size= STREAM_SIZEkB time= TIMESTAMP br= BITRATEkbits/s avg_br= AVERAGE_BITRATEkbits/s




out= OUT_FILE_INDEX st= OUT_FILE_STREAM_INDEX frame= FRAME_NUMBER q= FRAME_QUALITYf PSNR= PSNR f_size= FRAME_SIZE s_size= STREAM_SIZEkB time= TIMESTAMP br= BITRATEkbits/s avg_br= AVERAGE_BITRATEkbits/s




If you specify the input format and device then ffmpeg can grab video and audio directly.

ffmpeg -f oss -i /dev/dsp -f video4linux2 -i /dev/video0 /tmp/out.mpg

Or with an ALSA audio source (mono input, card id 1) instead of OSS:

ffmpeg -f alsa -ac 1 -i hw:1 -f video4linux2 -i /dev/video0 /tmp/out.mpg




Grab the X11 display with ffmpeg via

ffmpeg -f x11grab -video_size cif -framerate 25 -i :0.0 /tmp/out.mpg

0.0 is display.screen number of your X11 server, same as the DISPLAY environment variable.

ffmpeg -f x11grab -video_size cif -framerate 25 -i :0.0+10,20 /tmp/out.mpg





 You can use YUV files as input:

ffmpeg -i /tmp/test%d.Y /tmp/out.mpg

It will use the files:

/tmp/test0.Y, /tmp/test0.U, /tmp/test0.V,
/tmp/test1.Y, /tmp/test1.U, /tmp/test1.V, etc...

The Y files use twice the resolution of the U and V files. They are raw files, without header. They can be generated by all decent video decoders. You must specify the size of the image with the -s option if ffmpeg cannot guess it.
You can input from a raw YUV420P file:

ffmpeg -i /tmp/test.yuv /tmp/out.avi

test.yuv is a file containing raw YUV planar data. Each frame is composed of the Y plane followed by the U and V planes at half vertical and horizontal resolution.
You can output to a raw YUV420P file:

ffmpeg -i mydivx.avi hugefile.yuv

You can set several input files and output files:

ffmpeg -i /tmp/a.wav -s 640x480 -i /tmp/a.yuv /tmp/a.mpg

Converts the audio file a.wav and the raw YUV video file a.yuv to MPEG file a.mpg.
You can also do audio and video conversions at the same time:

ffmpeg -i /tmp/a.wav -ar 22050 /tmp/a.mp2

Converts a.wav to MPEG audio at 22050 Hz sample rate.
You can encode to several formats at the same time and define a mapping from input stream to output streams:

ffmpeg -i /tmp/a.wav -map 0:a -b:a 64k /tmp/a.mp2 -map 0:a -b:a 128k /tmp/b.mp2

Converts a.wav to a.mp2 at 64 kbits and to b.mp2 at 128 kbits. ’-map file:index’ specifies which input stream is used for each output stream, in the order of the definition of output streams.
You can transcode decrypted VOBs:

ffmpeg -i snatch_1.vob -f avi -c:v mpeg4 -b:v 800k -g 300 -bf 2 -c:a libmp3lame -b:a 128k snatch.avi

This is a typical DVD ripping example; the input is a VOB file, the output an AVI file with MPEG-4 video and MP3 audio. Note that in this command we use B-frames so the MPEG-4 stream is DivX5 compatible, and GOP size is 300 which means one intra frame every 10 seconds for 29.97fps input video. Furthermore, the audio stream is MP3-encoded so you need to enable LAME support by passing --enable-libmp3lame to configure. The mapping is particularly useful for DVD transcoding to get the desired audio language.

NOTE: To see the supported input formats, use ffmpeg -demuxers.
You can extract images from a video, or create a video from many images:

For extracting images from a video:

ffmpeg -i foo.avi -r 1 -s WxH -f image2 foo-%03d.jpeg

This will extract one video frame per second from the video and will output them in files named foo-001.jpeg, foo-002.jpeg, etc. Images will be rescaled to fit the new WxH values.

If you want to extract just a limited number of frames, you can use the above command in combination with the -frames:v or -t option, or in combination with -ss to start extracting from a certain point in time.

For creating a video from many images:

ffmpeg -f image2 -framerate 12 -i foo-%03d.jpeg -s WxH foo.avi







The syntax foo-%03d.jpeg specifies to use a decimal number composed of three digits padded with zeroes to express the sequence number. It is the same syntax supported by the C printf function, but only formats accepting a normal integer are suitable.

When importing an image sequence, -i also supports expanding shell-like wildcard patterns (globbing) internally, by selecting the image2-specific -pattern_type glob option.

For example, for creating a video from filenames matching the glob pattern foo-*.jpeg:

ffmpeg -f image2 -pattern_type glob -framerate 12 -i 'foo-*.jpeg' -s WxH foo.avi

You can put many streams of the same type in the output:

ffmpeg -i test1.avi -i test2.avi -map 1:1 -map 1:0 -map 0:1 -map 0:0 -c copy -y test12.nut

The resulting output file test12.nut will contain the first four streams from the input files in reverse order.
To force CBR video output:

ffmpeg -i myfile.avi -b 4000k -minrate 4000k -maxrate 4000k -bufsize 1835k out.m2v

The four options lmin, lmax, mblmin and mblmax use ’lambda’ units, but you may use the QP2LAMBDA constant to easily convert from ’q’ units:

ffmpeg -i src.ext -lmax 21*QP2LAMBDA dst.ext










