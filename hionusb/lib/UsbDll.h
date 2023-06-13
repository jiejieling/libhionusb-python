#ifndef _USBDLL_H_
#define _USBDLL_H_

// The following ifdef block is the standard way of creating macros which make exporting 
// from a DLL simpler. All files within this DLL are compiled with the USBDLL_EXPORTS
// symbol defined on the command line. this symbol should not be defined on any project
// that uses this DLL. This way any other project whose source files include this file see 
// USBDLL_API functions as being imported from a DLL, wheras this DLL sees symbols
// defined with this macro as being exported.
#ifdef USBDLL_EXPORTS
#define USBDLL_API __declspec(dllexport)
#else
#define USBDLL_API __declspec(dllimport)
#endif


#include <wtypes.h>
#include <initguid.h>

#define		RECORD_LOCAL 0
#define		RECORD_TALK  1
#define		RECORD_LY    2
// the following functions' definition and macros' definition are the APIs for USB protocol

//----from Phone to PC--------------------------

#ifndef WM_USER
#define WM_USER              0x0400
#endif

/*
//�豸����ʱ������Ϣ��ָUSB����PC���ն˵绰�����Ӻã�.
//����wParam��(BYTE)���;  lParam: 0L.
*/
#define WM_DEVICECONNECT	 WM_USER+701

/*
//�豸�Ͽ�ʱ������Ϣ��ָUSB����PC���ն˵绰����һ���Ͽ�ʱ������Ϣ��.
//����wParam��(BYTE)0L--ȫ���Ͽ�;  lParam: 0L.
//                  1L--�Ͽ�һ̨����;  lParam: (BYTE)���
*/	
#define WM_DEVICEDISCONNECT		WM_USER+702	

/*
//���н���,��ժ��ʱ���ʹ���Ϣ. 
//����wParam��(BYTE)���;  lParam: 0L.
*/
#define WM_OFFHOOK		WM_USER+703		

/*
//���жϿ������һ�ʱ���ʹ���Ϣ. 
//����wParam��(BYTE)���;  lParam: 0L--�һ���1L--�ն��ڱ�����״̬�°�������˳��˱���.
*/
#define WM_ONHOOK		WM_USER+704	
	
/*
//����ʱ�����������.
//����wParam��(BYTE)���;   lParam:char*.
//��ͨ�ĺ��볤��>1�����������1��������2���Ǵ������֡���������1���Ǵ������ܡ���
*/
#define WM_CALLERID		WM_USER+705		

/*
//�������巢����Ϣ.
//����wParam��(BYTE)���;    lParam: (BYTE)0x01����ʾһ�������죻0x00����ʾ�˴���������
*/
#define WM_RING		WM_USER+706		

/*
//ͨ�������У��յ�����DTMF��ֵʱ��������Ϣ.
//����wParam: (BYTE)���;	lParam: char.
*/
#define WM_KEY	WM_USER+707

/*
//���Թ����У����������绰��ֹͣ���ԣ�������Ϣ.
//����wParam: (BYTE)���;	lParam: 0L.
*/
#define WM_STOPLY	WM_USER+708

/*
//ͨ�������У��յ�����������������
//����wParam: (BYTE)���;	lParam: (BYTE)0x01--����������0x00--�����ر�.
*/
#define WM_MUTE		WM_USER+709



extern "C" {
//---------from PC to Phone-------------------------
// ����˵�����򷵻� 0 ����ɹ�
USBDLL_API int _stdcall InitDll();					//��ʼ����������һ��

USBDLL_API int _stdcall OffHookCtrl(int iDevIdx);					//����ժ������

USBDLL_API int _stdcall HangUpCtrl(int iDevIdx);					//���͹һ�����

USBDLL_API int _stdcall StartDial(int iDevIdx,const char* szDest);	//���Ͳ�������

USBDLL_API int _stdcall Bell(int iDevIdx,BYTE mode);					//�������忪���,mode: 0--�ر�; 1--��

USBDLL_API int _stdcall SendDTMF(int iDevIdx,const char* szDTMF);	//��StartDial��������,�����β�����

USBDLL_API int _stdcall BindWindow(HWND hwnd);			//�󶨴��ڣ������¼����͵��˴��ڣ���ʼ��ʱ���ã�ϵͳ������Ϣ WM_DEVICECHANGE ����ô˺���

USBDLL_API int _stdcall UnBindWindow();					//������ڰ�, �������¼������ᷢ�͵��˴��ڣ���������ʱ���ô˺���

USBDLL_API int _stdcall QueryPhoneStatus(int iDevIdx);			//��ѯ����ժ�һ�״̬ 0->�һ�,1->ժ��

USBDLL_API int _stdcall setLocalRecord(int iDevIdx,BOOL rec);	//����¼�������� pc ʱ�� rec: false--�ر�;true--�� 

USBDLL_API int _stdcall setTalkRecord(int iDevIdx,BOOL rec);		//ͨ��¼����rec: false--�ر�;true--�� 

USBDLL_API int _stdcall setLeaveRecord(int iDevIdx,BOOL rec);		//����¼����rec: false--�ر�;true--�� 

USBDLL_API int _stdcall GetSerialNo(int iDevIdx, char * number);	//��ȡ���к�

USBDLL_API int _stdcall SetSerialNo(int iDevIdx, const char * number);	//�������к�

USBDLL_API int _stdcall Flash(int iDevIdx,UINT ivalue);	//����һ�£�ivalue--Flash������ʱ�䳤��,ȡֵΪ0--100ms,1--180ms,2--300ms,3--600ms,4--1000ms֮�䡣

USBDLL_API int _stdcall SetDialTone(int iDevIdx,BYTE mode);				//���ò����������,mode: 0--�ر�; 1--��

USBDLL_API int _stdcall SetAutoAnswer(int iDevIdx,BYTE mode);			//�����Զ����������,mode: 0--�ر�; 1--��

USBDLL_API int _stdcall SetFlashTime(int iDevIdx,UINT ivalue);			//����Flashֵ, ivalue ȡֵΪ0--100ms,1--180ms,2--300ms,3--600ms,4--1000ms֮��

USBDLL_API int _stdcall SetOutcode(int iDevIdx, const char * code);		//���ó����룬���3λ

USBDLL_API int _stdcall StartRecordFile(int iDevIdx, const char* strFileName);	//��ʼ¼������, strFileName: ¼���ļ�����������·��
																		//��:"C:\\record\\sound.wav"��iType: ¼�����ͣ�0:����¼����1:ͨ��¼����2:����¼��

USBDLL_API int _stdcall StopRecordFile(int iDevIdx);	//ֹͣ¼��

USBDLL_API int _stdcall ZhuanBo(int iDevIdx,UINT ivalue);	//ת������һ�£�ivalue--ת��������ʱ�䳤��,ȡֵΪ0--100ms,1--180ms,2--300ms,3--600ms,4--1000ms֮�䡣

USBDLL_API int _stdcall Hold(int iDevIdx, BOOL bOn);	//bOn--1:����������0:�رձ���

USBDLL_API int _stdcall Mute(int iDevIdx, BOOL bOn);	// bOn->1:����������0:�رձ�����
}
#endif