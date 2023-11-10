#include <stdio.h>
#include <stdlib.h> 
#include <string.h>

int main(void){
	struct REG_0 reg_0;
	struct REG_0 *ptr = &reg_0;

	char band_sel[3];
	char band_sl[2];
	int band_sl_num;
	printf("%s","1. Output H,M,L band and number(ex: LB 3):");
	gets(band_sel);
	sscanf(band_sel, "%s %d", &band_sl, &band_sl_num);
	
	char pa_mode;
        printf("%s","2. Input H,L PA mode:");
	scanf("%c",&pa_mode);

	char lb_switch[2];
	printf("%s","3. Input H,M,L band : ");
	scanf("%s",lb_switch);

	int i = 0;
	switch(band_sl[0]){
		case 'L':
			for(i=1;i<5;i++){
				if(band_sl_num==i){
					ptr->band_select = i;
				}
			}
			break;
		case 'M':
			for(i=6;i<10;i++){
				if(band_sl_num==i-5){
					ptr->band_select = i;
				}
			}
			break;
		case 'H':
			for(i=11;i<13;i++){
				if(band_sl_num==i-10){
					ptr->band_select = i;
				}
			}
			break;
	}
	
	
	if(pa_mode=='H'){
		ptr->pa_mode = 0x00;
	}else{
		ptr->pa_mode = 0x01;
	}
	
	if(strcmp(lb_switch,"VL")==0){
		ptr->lb_switch = 0x01;
	}else{
		ptr->lb_switch = 0x00;
	}


	printf("Trigger:0x%X, Band:0x%X, PA enable:0x%X, PA mode:0x%X, LB switch:0x%X\n",ptr->trigger<<7,ptr->band_select<<3,ptr->pa_enable<<2,ptr->pa_mode<<1,ptr->lb_switch );
	int ans = ((ptr->trigger<<7)|(ptr->band_select<<3)|(ptr->pa_enable<<2)|(ptr->pa_mode<<1)|(ptr->lb_switch));
	printf("register value is : 0x%X\n",ans);

	return 0;
}
