%% mountain_sounds.m
% Make sounds with mountains!
% By Patrick "P-Sparx" Lloyd

%% Description
% This script reads in a greyscale image of an optical soundtrack and
% converts it to a binary image. Then, from left to right, it calculates
% frequency information from the difference between the top white pixel and
% the bottom white pixel in each column of the image.

% The corresponding sinusoids are generated and stacked end to end into a
% big freaking 1-dimensional vector. This vector is used to play the sound
% and then write that sound to a *.wav file.

%% Code

% Empty your mind of everything that doesn't have to do with fine dining.
% Fine dining and breathing.
clc;
clear;

% Constants
BOT_FREQ = 100;     % Lowest frequency that can be played
TOP_FREQ = 1500;    % Highest ""
Fs = 44100;         % CD quality sample rate = full retard oversampling

% Begin at the beginning
sound_image = imread('greyscale_mountain.bmp'); % Reads in our image
bw_image = im2bw(sound_image);      % Converts greyscale to binary
area = zeros(1, length(bw_image));  % Preallocate space for area vector

% (Approximate) desired play time per pixel
% 10/length(bw_image) = ~10 seconds total play time
play_time = 10/length(bw_image);

% Determine variable areas of the waveform
for i = 1:length(bw_image)    
    area(i) = ...
        abs(find(bw_image(:,i), 1, 'last') - ...
        find(bw_image(:,i), 1, 'first'));
end

% Determine the frequencies of each of the waves based on the areas
wave_freqs = area * (TOP_FREQ - BOT_FREQ) / 512;

% Generate x and y values for each frequency. Play time of each sine wave
% is rounded to the nearest full period. Then the x's and y's for each
% frequency get concatenated into big, dynamically resizing vectors (very
% slow and really bad form, but fuck it! I do what I want!)
xbig = 0;
ybig = 0;

for i = 1:length(wave_freqs)
    x = 0 : 1 / Fs : round(play_time*wave_freqs(i))/wave_freqs(i);
    y = sin(2*pi*wave_freqs(i)*x);
    
    xbig = [xbig x];
    ybig = [ybig y];
end

% Play the sounds and write ro file
sound(ybig', Fs);
wavwrite(ybig', Fs, 16, 'mountain_sounds.wav');

